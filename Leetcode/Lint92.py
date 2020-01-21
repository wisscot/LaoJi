# 92. Backpack

'''
Given n items with size Ai, an integer m denotes the size of a backpack. How full you can fill this backpack?

'''

Basic idea: DP
T[size][j] is max cap backpack can fill with size and items 0...j
T[size][j] = T(size, j-1) if A[i] > size
          max(T(size-A[i], i-1)+A[i], T(size, i-1))


Solution: 2d array 
class Solution:
    def backPack(self, m, A):
        n = len(A)
        f = [[False] * (m + 1) for _ in range(n + 1)]
        
        f[0][0] = True
        for i in range(1, n + 1):
            f[i][0] = True
            for j in range(1, m + 1):
                if j >= A[i - 1]:
                    f[i][j] = f[i - 1][j] or f[i - 1][j - A[i - 1]]
                else:
                    f[i][j] = f[i - 1][j]
                    
        for i in range(m, -1, -1):
            if f[n][i]:
                return i
        return 0


Solution: 1d array
class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """
    def backPack(self, m, A):
        # write your code here
        
        T = [False]*(m+1)
        T[0] = True
        res = 0
        for a in A:
            for i in range(m,0,-1):
                if i>=a and T[i-a]:
                    T[i] = True
                    res = max(res, i)
        return res


Solution: Top-down
class Solution:
    def backPack(self, m, A):
        # write your code here
        
        import functools
        @functools.lru_cache(None)
        def dp(size, i):
            if size <= 0:
                return 0
            if i < 0:
                return 0
            if A[i] > size:
                return dp(size, i-1)
            return max(dp(size-A[i], i-1)+A[i], dp(size, i-1))
        
        return dp(m, len(A)-1)