# 674. Longest Continuous Increasing Subsequence

'''
Given an unsorted array of integers, find the length of longest continuous increasing subsequence (subarray).

Example 1:
Input: [1,3,5,4,7]
Output: 3
Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3. 
Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4. 
'''

Basic idea: two pointers
Onwards


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        j = 0
        res = 0
        for i in range(len(nums)):
            if i and nums[i] <= nums[i-1]:
                j = i
            res = max(res, i-j+1)
        return res