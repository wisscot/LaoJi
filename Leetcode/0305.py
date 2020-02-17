# 305. Number of Islands II

'''
A 2d grid map of m rows and n columns is initially filled with water. We may perform an addLand operation which turns the water at position (row, col) into a land. Given a list of positions to operate, count the number of islands after each addLand operation. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
'''

Basic idea: Union Find
union node with adjecent nodes, count how many island


class UnionFind:
    def __init__(self):
        self.p = {}
        self.group = 0
        
    def find(self, u):
        if self.p[u] != u:
            self.p[u] = self.find(self.p[u])
        return self.p[u]
    
    def union(self, u, v):
        rootu = self.find(u)
        rootv = self.find(v)
        if rootu == rootv:
            return
        self.p[rootu] = rootv
        self.group -= 1
    
DIRECTIONS = [(1,0),(0,1),(-1,0),(0,-1)]
class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        grid = [[0]*n for _ in range(m)]
        
        uf = UnionFind()
        res = []
        for i, j in positions:
            if grid[i][j] == 1:
                res.append(uf.group)
                continue
                
            uf.group += 1
            uf.p[(i,j)] = (i,j)
            for di, dj in DIRECTIONS:
                i_, j_ = i + di, j + dj
                if not self.within(m, n, i_, j_):
                    continue
                if grid[i_][j_] == 0:
                    continue
                uf.union((i, j), (i_, j_))
            res.append(uf.group)
            grid[i][j] = 1
                
        return res
    
    def within(self, m, n, i, j):
        return 0<=i<m and 0<=j<n