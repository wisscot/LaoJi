# 312. Burst Balloons

'''
Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note:

You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
Example:

Input: [3,1,5,8]
Output: 167 
Explanation: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
             coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
'''

Basic idea:
We append 1 to the start and end of the array, which were invisible
Think about the last step, there will only one left in the middle
1                   ai                  1
so every burst between left 1 and ai will have left 1 and ai as fixed unburst boundary,
same applies to the right,
just like the boundary 1  ...  1  for the original problem,

So this problem becomes a subproblem, 
1 a0 a1 ....  ai-1  ai  ai+1 ....  1
---------------------
                    ----------------
Score(1 -> 1) = 1*ai*1 + Score(1 -> ai) + Score(ai -> 1 right side) 

Let T(left, right) be the max burst scores with left and right fixed,
then T(left, right) = a_left*ai*a_right + T(left, i) + T(right, i)

Then we go through all the ai to get the max

# Solution with Memoization
class Solution:
    """
    @param nums: A list of integer
    @return: An integer, maximum coins
    """
    def maxCoins(self, nums):
        # write your code here
        import functools
        
        @functools.lru_cache(None)
        def dp(left, right):
            if left > right-2:
                return 0
            if left == right-2:
                return nums[left]*nums[left+1]*nums[right]
            res = 0
            for mid in range(left+1, right):
                res = max(res, nums[left]*nums[mid]*nums[right] + 
                                dp(left, mid)+dp(mid, right))
            return res
            
        nums = [1] + nums + [1]
        return dp(0, len(nums)-1)      


# Solution Iterative DP
todo  

