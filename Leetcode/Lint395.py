# 395. Coins in a Line II

'''
There are n coins with different value in a line. Two players take turns to take one or two coins from left side until there are no more coins left. The player who take the coins with the most value wins.

Could you please decide the first player will win or lose?

If the first player wins, return true, otherwise return false.

Example
Example 1:

Input: [1, 2, 2]
Output: true
Explanation: The first player takes 2 coins.
Example 2:

Input: [1, 2, 4]
Output: false
Explanation: Whether the first player takes 1 coin or 2, the second player will gain more value.
'''


Basic idea: DP
Let T(i) be the max possible sum for values[i:]


Solution 1:
Two possibilities:
    1. take one coin
        then opponent will take one or two to minimize your later get
    2. take two coins
        then opponent will take one or two to minimize your later get
T(i) = max(   values[i]+min(T[i+2], T[i+3]), values[i]+values[i+1]+min(T(i+3),T(i+4))   )
Base case: T[-1] = values[-1]


Solution 2:
think from the second player, the max gain he/she can take is currsum - dp[i], right?
and he/she will have either dp[i+1] or dp[i+2], and the first player will try to minimize that

So, currsum - T[i] = min(T[i+1], T[i+2]) 

Time O(n)
Space O(n) can be reduced to O(1)


# Solution 1
class Solution:
    """
    @param values: a vector of integers
    @return: a boolean which equals to true if the first player will win
    """
    def firstWillWin(self, values):
        # write your code here

        import functools
        @functools.lru_cache(None)
        def dp(i):
            if i > len(values) - 1:
                return 0
            if i == len(values) - 1: #base case
                return values[i]
            return max(values[i]+min(dp(i+2),dp(i+3)), 
                       values[i]+values[i+1]+min(dp(i+3),dp(i+4)))
            
        return dp(0) > dp(1) or dp(0) > dp(2)


# Solution 2
class Solution:
    """
    @param values: a vector of integers
    @return: a boolean which equals to true if the first player will win
    """
    def firstWillWin(self, values):
        # write your code here
        postfixsum = [0]
        for val in values[::-1]:
            postfixsum.append(postfixsum[-1]+val)
        postfixsum = postfixsum[::-1]

        import functools
        @functools.lru_cache(None)
        def dp(i):
            if i > len(values) - 1:
                return 0
            if i == len(values) - 1: #base case
                return values[i]
            return postfixsum[i]-min(dp(i+1), dp(i+2))
            
        # return dp(0) > dp(1) or dp(0) > dp(2)
        return dp(0) > postfixsum[0] - dp(0)  # alternative way, verify current first take will be greater than opponent
