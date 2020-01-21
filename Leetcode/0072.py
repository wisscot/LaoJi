# 72. Edit Distance

Basic idea: DP
if the last char in two strings are the same, then...
if not, then ... 
basecase: the distance between an empty string and a len=m string is m

Time: O(mn)
Space: O(mn)  can reduce to O(n) using sliding array


class Solution:
    """
    @param word1: A string
    @param word2: A string
    @return: The minimum number of steps.
    """
    def minDistance(self, word1, word2):
        # write your code here
        
        import functools
        @functools.lru_cache(None)
        def dp(i,j):
            if i<0:
                return j+1
            if j<0:
                return i+1
            if word1[i] == word2[j]:
                return dp(i-1, j-1)
            return min(dp(i-1,j), dp(i,j-1), dp(i-1,j-1)) + 1
            
        return dp(len(word1)-1, len(word2)-1)
