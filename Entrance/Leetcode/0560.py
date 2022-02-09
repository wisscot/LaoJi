# 560. Subarray Sum Equals K
'''
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.
'''

Basic idea: prefix sum

find presum[j] - presum[i] = k for all j>i

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        presum = [0]
        for num in nums:
            presum.append(presum[-1]+num)
        
        count = collections.defaultdict(int)
        res = 0
        for prs in presum:
            res += count[prs-k]
            count[prs] += 1
            
        return res