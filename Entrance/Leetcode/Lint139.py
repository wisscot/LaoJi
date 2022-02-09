# 139. Subarray Sum Closes

'''
Given an integer array, find a subarray with sum closest to zero. Return the indexes of the first number and last number.
'''

Basic idea: Presum sort

class Solution:
    """
    @param: nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySumClosest(self, nums):
        # write your code here
        presum = [0]
        for num in nums:
            presum.append(presum[-1]+num)
        
        arr = sorted(list(enumerate(presum)), key=lambda tp:(tp[1],tp[0]))
        minval = float('inf')
        for i in range(1, len(arr)):
            gap = arr[i][1] - arr[i-1][1]
            if minval > gap:
                minval = gap
                left, right = arr[i][0], arr[i-1][0]
        if left > right:
            left, right = right, left
        return [left, right-1]
                    
        