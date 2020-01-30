# 153. Find Minimum in Rotated Sorted Array

'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2] 
Output: 1
'''

Basic idea: Binary Search


class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        # write your code here
        left, right = 0, len(nums)-1
        while left < right - 1:
            mid = (left+right)//2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid
        
        return min(nums[left], nums[right])