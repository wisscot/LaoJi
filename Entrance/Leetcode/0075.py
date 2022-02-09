# 75. Sort Colors

'''
Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
'''

Basic idea:
Partition into three parts: 0, 1, 2
with three pointers

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 0 0 0 0 1 1 1 2 1 2 2 1 0 2 2 2
        #         i     j         k
        i, j, k = 0, 0, len(nums) - 1
        while j <= k:
            if nums[j] == 0:
                self.swap(nums, i, j)
                i += 1
                j += 1
            elif nums[j] == 1:
                j += 1
            elif nums[j] == 2:
                self.swap(nums, j, k)
                k -= 1
                
    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]        
        