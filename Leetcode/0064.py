# 64. Minimum Path Sum

'''
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
'''

A typical DP problem 

Basic idea:
Let T(i,j) be the result (mininum path sum) at (i,j), then
T(i,j) = min{T(i-1,j), T(i,j-1)} + grid[i-1][j-1]
Base case: T(i, j) = 0 for i == 0 or j == 0

Solution 1: with lru_cache(None)
class Solution:
    """
    @param grid: a list of lists of integers
    @return: An integer, minimizes the sum of all numbers along its path
    """
    def minPathSum(self, grid):
        # write your code here
        import functools

        @functools.lru_cache(None)
        def dp(i, j):
            if i == 0 and j == 0:
                return grid[0][0]
                
            if i == -1 or j == -1:
                return float('inf')
                
            return grid[i][j] + min(dp(i-1,j), dp(i,j-1))
            
        return dp(len(grid)-1, len(grid[0])-1)
        
        
Solution 2: with array
class Solution:
    """
    @param grid: a list of lists of integers
    @return: An integer, minimizes the sum of all numbers along its path
    """
    def minPathSum(self, grid):
        # write your code here
        m, n = len(grid), len(grid[0])
        T = [[float('inf')]*(n+1) for _ in range(m+1)]
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if i == j == 1:
                    T[i][j] = grid[0][0]
                    continue
                T[i][j] = min(T[i-1][j], T[i][j-1]) + grid[i-1][j-1]
                
        return T[-1][-1]
        
        
Solution 2 - Improve 1: Space can be optimized
because only two rows in T are needed

class Solution:
    """
    @param grid: a list of lists of integers
    @return: An integer, minimizes the sum of all numbers along its path
    """
    def minPathSum(self, grid):
        # write your code here
        m, n = len(grid), len(grid[0])
        T = [[float('inf')]*(n+1) for _ in range(2)]
                                                 ^   
                                         # update from Solution 2
        for i in range(1, m+1):
            for j in range(1, n+1):
                if i == j == 1:
                    T[i][j] = grid[0][0]
                    continue
                T[i%2][j] = min(T[(i-1)%2][j], T[i%2][j-1]) + grid[i-1][j-1] # don't change grid[i-1] !
                   ^                   ^          ^   
                
        return T[i%2][-1]