# Kth Largest

## Heapq

```python
# Time O(klogn)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        nums = [-num for num in nums]
        heapq.heapify(nums)
        
        for _ in range(k):
            res = -heapq.heappop(nums)
            
        return res
```

## Quick Select

```python
# Time O(n) average, O(n^2) worst

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

```python
# Another intuitive way, refer to QuickSort intuitive implementation
```

## Find top K largest/smallest number 

- Solution 0: Brute Force, Find max, remove, repeat (offline) \
  Time O(nk)

- Solution 1: Sort and get first K (offline)    \
  Time O(nlogn)

- Solution 2: Min heap and get first K (offline)    \
  Time O(n + Klogn) \
  Time O(nlogn)    (online)

- Solution 3: Max heap (len==k) and get all (online)    \
  Time O(nlogK)

- Solution 4: quick select, find kth, then loop once, sort (Offline)    \
  Time O(n + KlogK)

## Examples

[215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)

[324. Wiggle Sort II](https://leetcode.com/problems/wiggle-sort-ii/)\
Find median in O(n)

[973. K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/)
0210G\
Top K minimum, 5 solutions