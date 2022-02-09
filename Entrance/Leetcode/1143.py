# 1143. Longest Common Subsequence

Basic idea: DP
check if last char is the same,
if yes, remove last char from both strings, 
if no, remove last char from either string, get max

class Solution:
    """
    @param A: A string
    @param B: A string
    @return: The length of longest common subsequence of A and B
    """
    def longestCommonSubsequence(self, A, B):
        # write your code here
        
        import functools
        @functools.lru_cache(None)
        def dp(i,j):
            if i<0 or j<0:
                return 0
            if A[i] == B[j]:
                return dp(i-1,j-1) + 1
            return max(dp(i-1,j), dp(i,j-1))
            
        return dp(len(A)-1, len(B)-1)
        
