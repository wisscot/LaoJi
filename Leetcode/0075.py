# 75. Sort Colors

'''
Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
'''

Solution 1
Partition into three parts: lt, eq, gt
with three pointers, left, right and i

class Solution:
    def sortColors(self, nums):
        # write your code here
        
        left, right = 0, len(nums) - 1
        i = 0
        while i <= right:
            # lllllleeeeeelge.......gggggggg
            #       ^     ^        ^
            #       l     i        r         
            if nums[i] == 1:
                i += 1
                continue
            elif nums[i] == 0:
                self.swap(nums, i, left)
                left += 1
                i += 1
            else:
                self.swap(nums, i, right)
                right -= 1
                
    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]
        
        
        
Solution 2: 
Partition into two parts