# 33. Search in Rotated Sorted Array

'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).
'''

Basic idea: Binary Search

Solution 1: 
use '153. Find Minimum in Rotated Sorted Array' find the pivot point
then do binary search in one half part

Solution 2:
Binary search directly 


# Solution 2
class Solution:
    """
    @param A: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """
    def search(self, A, target):
        # write your code here
        if not A:
            return -1
        left, right = 0, len(A) - 1
        bar = A[-1]
        while left < right - 1:
            mid = (left+right)//2
            curr = A[mid]
            if curr > bar:
                if A[left] <= target <= curr:
                    right = mid
                else:
                    left = mid
            else:
                if curr <= target <= A[right]:
                    left = mid
                else:
                    right = mid
        
        if A[left] == target:
            return left
        if A[right] == target:
            return right
        return -1
