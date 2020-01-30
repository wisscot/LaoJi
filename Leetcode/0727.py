# 727. Minimum Window Subsequence

'''
Given strings S and T, find the minimum (contiguous) substring W of S, so that T is a subsequence of W.

If there is no such window in S that covers all characters in T, return the empty string "". If there are multiple such minimum-length windows, return the one with the left-most starting index.
'''

Basic idea: DP

class Solution:
    def minWindow(self, S: str, T: str) -> str:
        
        m, n = len(S), len(T)
        
        import functools
        @functools.lru_cache(None)
        def dp(i,j):
            if j == -1:
                return 0
            if i < j:
                return float('inf')
            if S[i] == T[j]:
                return dp(i-1, j-1) + 1
            else:
                return dp(i-1, j) + 1
            
        minlens = [dp(i,n-1) for i in range(m)]
        mintup = list(enumerate(minlens))
        mintup.sort(key=lambda x:(x[1], x[0]))
        idx, length = mintup[0]
        if length < float('inf'):
            return S[idx-length+1:idx+1]
        return ''

