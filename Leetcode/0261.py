# 261. Graph Valid Tree

'''
Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.
'''


Basic idea:

Solution 1:
BFS
visited from any node, if no cycle detected and all nodes will be visted, then its a tree

Solution 2:
Union Find
A graph is tree iff
    1. num of edges is n-1
    2. only one connected block


# Solution 1
class Solution:
	def validTree(self, n: int, edges: List[List[int]]) -> bool:
		if len(edges) != n - 1:
			return False
		
		graph = self.build_graph(n, edges)
		
		queue = collections.deque([0])
		visited = set([0])	
		while queue:
			node = queue.popleft()
			for child in graph[node]:
				if child in visited:
					continue
				queue.append(child)
				visited.add(child)
		
		return len(visited) == n

	def build_graph(self, n, edges):
		graph = {node:[] for node in range(n)}
		for n1, n2 in edges:
			graph[n1].append(n2)
			graph[n2].append(n1)
		return graph			


# Solution 2
class UnionFind:
    def __init__(self, n):
        self.p = list(range(n))
        self.size = [1]*n
        self.numBlock = n
        
    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]
        
    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            self.p[rootx] = rooty
            self.size[rooty] += self.size[rootx]
            self.numBlock -= 1
    
class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def validTree(self, n, edges):
        # write your code here
        if len(edges) != n-1:
            return False
            
        uf = UnionFind(n)
        for v1, v2 in edges:
            uf.union(v1, v2)
        
        return uf.numBlock == 1