# 1197. Minimum Knight Moves

'''
In an infinite chess board with coordinates from -infinity to +infinity, you have a knight at square [0, 0].

A knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.
'''

Basic idea:
The move is symmetric top bottom and left right and along y=x
so we only have to consider 1/8 of the whole domain

Solution 1:
BFS from (0,0)

Solution 2:
DP from target

# Solution 1
DIRECTIONS = [(1,2),(2,1),(1,-2),(-2,1),(-1,-2),(-2,-1),(-1,2),(2,-1)]
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        
        res = -1
        x, y = abs(x), abs(y)
        x, y = max(x, y), min(x, y)
        
        queue = collections.deque([(0,0)])
        visited = set([(0,0)])
        
        while True:
            res += 1
            for _ in range(len(queue)):
                pos = queue.popleft()
                if pos == (x,y):
                    return res
                for i, j in self.next_pos(pos):
                    if (i,j) in visited:
                        continue
                    queue.append((i,j))
                    visited.add((i,j))
        
    def next_pos(self, pos):
        posi, posj = pos
        res = set()
        for di, dj in DIRECTIONS:
            i = abs(posi + di)
            j = abs(posj + dj)
            newpos = (max(i,j), min(i,j))
            res.add((newpos))
        return res
                
                
        