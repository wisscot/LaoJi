# 305. Number of Islands II

'''
A 2d grid map of m rows and n columns is initially filled with water. We may perform an addLand operation which turns the water at position (row, col) into a land. Given a list of positions to operate, count the number of islands after each addLand operation. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
'''

Basic idea: Union Find
union node with adjecent nodes, count how many island


class UnionFind:
    def __init__(self, n):
        self.p = list(range(n))
        self.islandnum = 0
    
    def find(self, x): # path compression
        if x!= self.p[x]:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return
        self.p[rx] = ry
        self.islandnum -= 1

DIRECTIONS = [(1,0), (0,1), (-1,0), (0,-1)]
class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        def indexof(i,j):
            return i*n + j
        
        uf = UnionFind(m*n)
        grid = [[0]*n for _ in range(m)]
        
        res = []
        for pos in positions:
            i, j = pos
            if grid[i][j] == 1:
                res.append(uf.islandnum)
                continue
                
            uf.islandnum += 1
            grid[i][j] = 1
            for di, dj in DIRECTIONS:
                i_ = i + di
                j_ = j + dj
                if not self.within(i_, j_, m, n):
                    continue
                if grid[i_][j_] == 0:
                    continue
                uf.union(indexof(i,j), indexof(i_, j_))
            
            res.append(uf.islandnum)

        return res
            
    def within(self, x, y, m, n):
        return 0 <= x < m and 0 <= y < n