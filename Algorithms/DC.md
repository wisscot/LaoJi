# Divide and Conquer

## Overview
Divide a problem into two or more sub-problems of the same or related type


## Sorting Example

[912. Sort an Array](https://leetcode.com/problems/sort-an-array/)

## Quick Sort

Code1: easy to explain, use more space
```python
def quicksort(self, nums):
    if len(nums) <= 1:
        return nums

    pivot = random.choice(nums)
    lt = [v for v in nums if v < pivot]
    eq = [v for v in nums if v == pivot]
    gt = [v for v in nums if v > pivot]

    return self.quicksort(lt) + eq + self.quicksort(gt)
```

Code2: typical
Time: O(nlogn) Space:O(1)
```python
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quicksort(nums, 0, len(nums)-1)
        return nums
    
    def quicksort(self, nums, left, right):
    
        if left >= right:
            return 
        pivot = nums[right]
        # ssssssssbbbbbsbssbbbbp
        # l       j    i       r
        j = left  # Do NOT assign 0 to j
        for i in range(left, right): 
            if nums[i] < pivot:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
        nums[right], nums[j] = nums[j], nums[right] # not nums[-1]
        # sssssspbbbbbbbbb
        # l     j        r
        self.quicksort(nums, left, j-1)
        self.quicksort(nums, j+1, right)
```
