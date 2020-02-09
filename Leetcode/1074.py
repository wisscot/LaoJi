# 1074. Number of Submatrices That Sum to Target

'''
Given a matrix, and a target, return the number of non-empty submatrices that sum to target.

A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x <= x2 and y1 <= y <= y2.

Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if they have some coordinate that is different: for example, if x1 != x1'.
'''


Basic idea: Prefix sum

Solution 1:
calculation matrix prefix sum
then enumerate left top corners and right bottom corners 
Time: O((mn)^2)

Solution 2:
fix row i,j
treat col[i...j] as one tall cell
then we can reduce it to subarray prefixsum
Time: O(m*m*n)

# Solution 2
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])
        
        res = 0
        for i in range(m):
            tall_cells = [0] * n
            for j in range(i, m):
                for k in range(n):
                    tall_cells[k] += matrix[j][k]
                res += self.numSubarraySum(tall_cells, target)
        return res
    
    def numSubarraySum(self, arr, target):

        presum = list(arr)
        n = len(arr)
        for k in range(1, n):
            presum[k] += presum[k-1]

        res = 0
        count = collections.Counter({0:1})
        for num in presum:
            if num - target in count:
                res += count[num-target]
            count[num] += 1
            
        return res