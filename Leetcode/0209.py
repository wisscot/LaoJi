# 209. Minimum Size Subarray Sum
Solution 1. Brute force
  Basic idea: enumerate all combination of i, j , sum from i to j
  Time O(n^3)
  With prefix sum
  Time reduced to O(n^2)
  We can do Binary Search in prefix sum
  Time reduced to O(nlogn)
  
 Solution 2. Two Pointers
  Basic idea: 
  use i, j as the sum range, if range[i to j] meets the target, then for increasing j', i' must be > i
  so we can use same direction two pointers

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        # write your code here
        
        # i and j are inclusive
        i = 0
        res = float('inf')
        curr_sum = 0
        for j in range(len(nums)):
            curr_sum += nums[j]
            while i <= j and curr_sum >= s:
                res = min(res, j-i+1)
                curr_sum -= nums[i]
                i += 1
        
        return res if res<float('inf') else -1
