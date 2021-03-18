# 644. Maximum Average Subarray II

'''
Given an array consisting of n integers, find the contiguous subarray whose length is 
greater than or equal to k that has the maximum average value. And you need to output the maximum average value.

Example 1:
Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation:
when length is 5, maximum average value is 10.8,
when length is 6, maximum average value is 9.16667.
Thus return 12.75.
'''


Basic idea:
if we propose a solution T, we can verify that 
if there exists a subarray (len>=k) with mean >= T,
then we can use binary search on result

how to verify that?
if exists a subarray [Ai, Ai+1, ..., Aj] that Ai + Ai+1 +... + Aj / (j-i+1) >= T
that is (Ai - T) + (Ai+1 - T) + ... + (Aj - T) >= 0
so this becomes a subarray sum problem, which we can use prefix sum to solve

Algorithm: binary search + two pointer
Time complexity: O(n*log((maxVal-minVal)/1e-5))


class Solution:
    """
    @param nums: an array with positive and negative numbers
    @param k: an integer
    @return: the maximum average
    """
    def maxAverage(self, nums, k):
        # write your code here
        lower, upper = min(nums), max(nums)
        
        while lower < upper - 1e-5:
            mid = (lower+upper)/2
            if self.canfind(nums, mid, k): # if meet target, go toward requirement (max)
                lower = mid
            else:
                upper = mid
                
        if self.canfind(nums, upper, k): # to find maximum check upper first
            return upper
        return lower
        
    def canfind(self, nums, targetmean, k):
        
        arr = [num-targetmean for num in nums]
        prefixsum = [0]
        for num in arr:
            prefixsum.append(num+prefixsum[-1])
        
        leftmin = 0
        for i in range(k, len(prefixsum)):
            leftmin = min(leftmin, prefixsum[i-k])
            currsum = prefixsum[i] - leftmin
            if currsum >= 0:
                return True
        return False
            