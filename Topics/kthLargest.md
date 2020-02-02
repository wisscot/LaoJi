# Kth Largest

## Heapq

Time O(klogn)
```python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        nums = [-num for num in nums]
        heapq.heapify(nums)
        
        for _ in range(k):
            res = -heapq.heappop(nums)
            
        return res
```

## Quick Select

Time O(n) average, O(n^2) worst
```python
def quick_select(self, nums, k, left, right):
    pivot = nums[right]
    # ...ssssssbbbbbbsbsbsbp...
    #    l     j     i     r
    j = left
    for i in range(left, right):
        if nums[i] > pivot:
            self.swap(nums, i, j)
            j += 1
    self.swap(nums, j, right)
    # ...sssssspbbbbbbbbbbbb...
    #    l     j          ir
    if k <= j-left:
        return self.find(nums, k, left, j-1)
    if k > j+1-left:
        return self.find(nums, k-(j+1-left), j+1, right)
    return pivot
``` 

__Examples:__

[215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)  \


## Examples

[324. Wiggle Sort II](https://leetcode.com/problems/wiggle-sort-ii/)\
Find median in O(n)

