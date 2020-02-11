class UnionFind:
	def __init__(self):
		self.p = {}
		self.islandnum = 0
	
	def find(self, x): # path compression
		if x!= self.p[x]:
			self.p[point] = self.find(self.p[point])
		return self.p[point]

	def union(self, x, y):
		rx, ry = self.find(x), self.find(y)
		if rx == ry:
			return
		self.p[rx] = ry
		self.islandnum -= 1

DIRECTIONS = [(1,0), (0,1), (-1,0), (0.-1)]
class Solution:
	def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
	
        uf = UnionFind()
        visited = set()

        for pos in positions:
            uf.islandnum += 1
            x, y = pos
            for dx, dy in DIRECTIONS:
                x_ = x + dx
                y_ = y + dy
                if not self.within(x_, y_, m, n):
                    continue
                if (x_, y_) not in visited:
                    continue
                uf.union((x,y), (x_, y_))

            visited.add((x,y))

        return uf.islandnum
			
	def within(self, x, y, m, n):
		return 0 <= x < m and 0 <= y < n