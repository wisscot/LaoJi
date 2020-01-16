# 394. Coins in a Line

'''
There are n coins in a line. Two players take turns to take one or two coins from right side until there are no more coins left. The player who take the last coin wins.

Could you please decide the first player will win or lose?

If the first player wins, return true, otherwise return false.

Have you met this question in a real interview?  
Example
Example 1:

Input: 1
Output: true
Example 2:

Input: 4
Output: true
Explanation:
The first player takes 1 coin at first. Then there are 3 coins left.
Whether the second player takes 1 coin or two, then the first player can take all coin(s) left.
Challenge
O(n) time and O(1) memory
'''

Basic idea:
For a certain number of coins, there is a state that this situation will definitely win/lose (True/False)
if we take one coin, the next situation is definitely lose, then current situation is a win,
if we take two coins, and the next situation is definitely lose, then current situation is also a win,
So current = 'after taken one coin is lose'  or  'after taken two coins is lose'
Base case: if there is one or two left, its a definitely win

Time: O(n)
Space: O(n) can reduced to O(1)

class Solution:
    """
    @param n: An integer
    @return: A boolean which equals to true if the first player will win
    """
    def firstWillWin(self, n):
        # write your code here
        if not n:
            return False
        
        import functools
        @functools.lru_cache(None)
        def dp(n):
            if n==1 or n==2:
                return True
            return dp(n-1) == False or dp(n-2) == False
        
        return dp(n)
