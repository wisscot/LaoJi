# 16. 3Sum Closest

'''
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''

Basic idea: Two Pointers
loop i through the array, it becomes Two Sum Closest


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        
        res = float('inf')
        
        for i in range(len(nums)-2):
            left, right = i+1, len(nums) - 1
            target_new = target - nums[i]
            while left < right:
                curr_sum = nums[left]+nums[right]+nums[i]
                if abs(curr_sum-target) < abs(res-target):
                    res = curr_sum
                if nums[left]+nums[right] > target_new:
                    right -= 1
                else:
                    left += 1
                    
        return res