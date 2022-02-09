# 396. Coins in a Line III

'''There are n coins in a line, and value of i-th coin is values[i].

Two players take turns to take a coin from one of the ends of the line until there are no more coins left. The player with the larger amount of money wins.

Could you please decide the first player will win or lose?

Example 1:

Input: [3, 2, 2]
Output: true
Explanation: The first player takes 3 at first. Then they both take 2.
Example 2:

Input: [1, 20, 4]
Output: false
Explanation: The second player will take 20 whether the first player take 1 or 4.
'''

Basic idea: same as II

class Solution:
    """
    @param values: a vector of integers
    @return: a boolean which equals to true if the first player will win
    """
    def firstWillWin(self, values):
        # write your code here
        prefixsum = [0]
        for val in values:
            prefixsum.append(prefixsum[-1]+val)
            
        def sum(i, j):
            # inclusive
            return prefixsum[j+1] - prefixsum[i]
        
        import functools
        @functools.lru_cache(None)
        def dp(i,j):
            if i == j:
                return values[i]
            option1 = values[i] + sum(i+1,j) - dp(i+1,j)
            option2 = values[j] + sum(i,j-1) - dp(i,j-1)
            return max(option1, option2)
        
        return dp(0, len(values)-1)*2 > sum(0, len(values)-1)