# 300. Longest Increasing Subsequence

'''
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
'''

Solution 1: DP
for LIS ends at ith element T[i],
we go through all element to the left of i, if element j less than i, update T[j]+1 to T[i]
Time: O(n^2)


Solution 2: DP with Binary Search
keep an array with increasing order, replace it using current element
Time: O(nlogn)


# Solution 1
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0
        
        dp = [1] * len(nums)
        for i in range(len(nums)):
            currLIS = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    currLIS = max(currLIS, dp[j]+1)
            dp[i] = currLIS
        return max(dp)


# Solution 2
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cands = []
        for num in nums:
            idx = bisect.bisect_left(cands, num)
            cands[idx:idx+1] = [num]
        return len(cands)