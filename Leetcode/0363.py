# 363. Max Sum of Rectangle No Larger Than K

'''
Given a non-empty 2D matrix matrix and an integer k, find the max sum of a rectangle in the matrix such that its sum is no larger than k.

Example:

Input: matrix = [[1,0,1],[0,-2,3]], k = 2
Output: 2 
Explanation: Because the sum of rectangle [[0, 1], [-2, 3]] is 2,
             and 2 is the max number no larger than k (k = 2).
'''

Basic idea:
Convert 2D presum problem to 1D 

To solve a 1D subarray sum problem,
convert array to prefix sum

prefix sum array:
[0, 1, 5, -3, ..., 2, 9]
       ^           ^ 
       s1          s2
the goal is to find all s2 - s1 <= target and maximize s2 - s1
if we fix s2, then we need to find s1 >= s2 - target and minimize s1

So the idea to build a segment tree,
add nums before s2 into the tree, 
then query the minimum number in the range [s2-target, ∞)

Time Complexity:
m^2*nlogn
where m, n is the number of rows and cols,
if there are more rows than cols, transpose the matrix



Solution 1: Brute Force
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        
        target = k
        
        res = float('-inf')
        m, n = len(matrix), len(matrix[0])
                
        for i in range(m):
            tallCells = [0] * n
            for j in range(i, m):
                for k in range(n):
                    tallCells[k] += matrix[j][k]
                curr = self.maxsumArray(tallCells, target)
                res = max(curr, res)
        
        return res
    
    def maxsumArray(self, nums, target):
        presum = [0]
        for num in nums:
            presum.append(presum[-1]+num)
            
        res = float('-inf')
        for i in range(len(presum)):
            for j in range(i+1, len(presum)):
                curr = presum[j] - presum[i]
                if curr <= target:
                    res = max(res, curr)
        return res
                

Solution 2: 2d presum + Segment tree
INF = float('inf')

class SegTree:
    
    def __init__(self, start_i, end_i, nums):
        self.start, self.end = nums[start_i], nums[end_i]
        self.minval = INF
        self.left, self.right = None, None
        if start_i < end_i:
            mid = (start_i + end_i) // 2
            self.left = SegTree(start_i, mid, nums)
            self.right = SegTree(mid+1, end_i, nums)
            
    @classmethod
    def add_num(cls, root, num):
        if root is None:
            return
        if root.start <= num <= root.end:
            root.minval = min(root.minval, num)
            cls.add_num(root.left, num)
            cls.add_num(root.right, num)
            
    @classmethod
    def query(cls, root, start, end):
        if start <= root.start and root.end <= end:
            return root.minval
        if start > root.end or end < root.start:
            return INF
        return min(cls.query(root.left, start, end),
                   cls.query(root.right, start, end))
    
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], target: int) -> int:
                
        res = float('-inf')
        m, n = len(matrix), len(matrix[0])
        
        if m > n:
            matrix = self.transpose(matrix)
            m, n = n, m
        
        for i in range(m):
            tallCells = [0] * n
            for j in range(i, m):
                for k in range(n):
                    tallCells[k] += matrix[j][k]
                curr = self.maxsumArray(tallCells, target)
                res = max(curr, res)
        
        return res
    
    def maxsumArray(self, nums, target):
        presum = [0]
        for num in nums:
            presum.append(presum[-1]+num)
            
        uni_presum = sorted(set(presum))
        root = SegTree(0, len(uni_presum)-1, uni_presum)
        res = float('-inf')
        for i in range(len(presum)):
            minval = SegTree.query(root, presum[i]-target, INF)
            if minval < INF:
                res = max(res, presum[i] - minval)
            SegTree.add_num(root, presum[i])
            
        return res
                
    def transpose(self, matrix):
        m, n = len(matrix), len(matrix[0])
        matrix_ = [[0] * m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                matrix_[j][i] = matrix[i][j]
        return matrix_
