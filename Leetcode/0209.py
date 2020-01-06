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
  i is the master pointer - for loop
  j is the slave pointer - while loop

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        # write your code here
        
        res = float('inf')
        curr_sum = 0
        j = 0
        for i in range(len(nums)):
            # move j until cannot
            while j < len(nums) and curr_sum < s:
                curr_sum += nums[j]
                j += 1
            # save result
            if curr_sum >= s:
                res = min(res, j-i)
            # move i
            curr_sum -= s[i]
        
        return res if res<float('inf') else -1
