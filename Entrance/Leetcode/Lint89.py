# 89. k Sum

Basic idea: DP

class Solution:
    """
    @param A: An integer array
    @param k: A positive integer (k <= length(A))
    @param target: An integer
    @return: An integer
    """
    def kSum(self, A, k, target):
        # write your code here
        
        import functools
        @functools.lru_cache(None)
        def dp(i,j,t):
            if i<0:
                return 0
            if j<=0:
                return 0
            if t<=0:
                return 0
            if A[i] == t and j == 1:
                return 1
            
            if A[i]>target:
                return dp(i-1, j, t)
            return dp(i-1, j, t) + dp(i-1, j-1, t-A[i])

        return dp(len(A)-1, k, target)