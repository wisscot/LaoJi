# 1. Two Sum

'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

Solution 1: Brute Force
check every pairs of the nums
Time: O(n^2)  Space: O(1)

Solution 2: Sort
Sort and then use two pointers
Time: O(nlogn)  Space: O(1)

Solution 3: dict
use dict to save numbers visited
Time: O(n)  Space: O(n)


# Solution 1
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
                
    
# Solution 2
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tups = sorted(enumerate(nums), key=lambda tp:tp[1])
        
        i, j = 0, len(tups) - 1
        while i < j:
            left_idx, left_num = tups[i]
            right_idx, right_num = tups[j]
            if left_num + right_num < target:
                i += 1
            elif left_num + right_num > target:
                j -= 1
            else:
                return [left_idx, right_idx]
            
         
# Solution 3
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        for i, num in enumerate(nums):
            if target - num in visited:
                return [i, visited[target - num]]
            visited[num] = i