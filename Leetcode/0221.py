# 221. Maximal Square

'''
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
'''

Basic idea: DP

class Solution:
    """
    @param matrix: a matrix of 0 and 1
    @return: an integer
    """
    
    def maxSquare(self, matrix):
        # write your code here
        res = 0

        import functools
        @functools.lru_cache(None)
        def dp(i,j):
            if i<0 or j<0 or matrix[i][j] == 0:
                return 0
            return  1+min(dp(i-1,j-1), dp(i-1,j), dp(i,j-1))
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res = max(res, dp(i,j))
                
        return res**2
