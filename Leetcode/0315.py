# Solution 1. Segment Tree
     
class SegTree:
    def __init__(self, start_i, end_i, nums):
        self.start, self.end = nums[start_i], nums[end_i]
        self.left, self.right = None, None
        self.count = 0
        if start_i < end_i:
            mid = (start_i+end_i)//2
            self.left = SegTree(start_i, mid, nums)
            self.right = SegTree(mid+1, end_i, nums)
            
    @classmethod
    def update(cls, root, val):
        if not root:
            return
        if root.start <= val <= root.end:
            root.count += 1
            cls.update(root.left, val)
            cls.update(root.right, val)
            
    @classmethod
    def query(cls, root, start, end):
        if start <= root.start <= root.end <= end:
            return root.count
        if start > root.end or end < root.start:
            return 0
        return cls.query(root.left, start, end) + cls.query(root.right, start, end)
        
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []
        
        nums_sorted = sorted(set(nums))
        root = SegTree(0, len(nums_sorted)-1, nums_sorted)
        
        res = []
        for num in nums[::-1]:
            res.append(SegTree.query(root, float('-inf'), num-1))
            SegTree.update(root, num)
        
        return res[::-1]  
    

# Solution 2: Binary Indexed Tree

class FenTree:
    def __init__(self, n):
        self.arr = [0] * (n+1)
        self.n = n
        
    def add(self, idx, val):
        idx += 1
        while idx <= self.n:
            self.arr[idx] += val
            idx += idx & (-idx)
    
    def prefix_sum(self, idx):
        idx += 1
        res = 0
        while idx > 0:
            res += self.arr[idx]
            idx -= idx & (-idx)
        return res
    
    def range_sum(self, i, j):
        # inclusive
        return self.prefix_sum(j) - self.prefix_sum(i-1)
 
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []
        
        num_index = [(num, i) for i, num in enumerate(nums)]
        num_index.sort()
        indexs = [x[1] for x in num_index]
        
        # root = SegTree(min(indexs), max(indexs))
        n = len(indexs)
        fentree = FenTree(n+1)
        
        res = [0]*len(indexs)
        max_index = max(indexs)
        for index in indexs:
            res[index] = fentree.range_sum(index+1, max_index)
            fentree.add(index, 1)
        
        return res  