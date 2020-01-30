# 162. Find Peak Element

'''
A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
'''

Basic idea: Binary Search

check slope

class Solution:
    """
    @param A: An integers array.
    @return: return any of peek positions.
    """
    def findPeak(self, A):
        # write your code here
        left, right = 1, len(A)-2
        while left < right - 1:
            mid = (left+right)//2
            if self.slop(A, mid) == 1:
                left = mid
            elif self.slop(A, mid) == -1:
                right = mid
            elif self.slop(A, mid) == 0:
                return mid
                
        if self.slop(A, left) == 0:
            return left
        return right
        
    def slop(self, A, i):
        lval, rval = A[i-1], A[i+1]
        curr = A[i]
        if lval < curr < rval:
            return 1
        if rval < curr < lval:
            return -1
        if curr > max(lval, rval):
            return 0
        return 1
                
