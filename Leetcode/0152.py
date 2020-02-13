# 152. Maximum Product Subarray

'''
Find the contiguous subarray within an array (containing at least one number) which has the largest product.
Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
'''

Basic idea: DP
use current min and max as states

class Solution:
    """
    @param nums: An array of integers
    @return: An integer
    """
    def maxProduct(self, nums):
        # write your code here
        if not nums:
            return 0
        
        prev_max = prev_min = res = nums[0]
        
        for num in nums[1:]:
            if num > 0:
                curr_max = max(prev_max*num, num)
                curr_min = min(prev_min*num, num)
            else:
                curr_max = max(prev_min*num, num)
                curr_min = min(prev_max*num, num)
        
            res = max(res, curr_max)
            
            prev_max = curr_max
            prev_min = curr_min
            
        return res
        