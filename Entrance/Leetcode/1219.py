# 1219. Path with Maximum Gold

'''
In a gold mine grid of size m * n, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.
'''

Basic idea: DFS


DIRECTIONS = [(0,1), (0,-1), (1,0), (-1,0)]
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        
        res = [0, 0] # path, res
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                self.search(grid, i, j, res)
                
        return res[1]
    
    def search(self, grid, i, j, res):
        # assume (i,j) is valid
        if grid[i][j] == 0:
            return
        
        curr_val = grid[i][j]
        res[0] += curr_val
        res[1] = max(res)
        grid[i][j] = 0
        for di, dj in DIRECTIONS:
            i_, j_ = i + di, j + dj
            if not self.within(grid, i_, j_):
                continue
            self.search(grid, i_, j_, res)
            
        grid[i][j] = curr_val
        res[0] -= grid[i][j]
        
    def within(self, grid, i, j):
        return 0<=i<len(grid) and 0<=j<len(grid[0])
        