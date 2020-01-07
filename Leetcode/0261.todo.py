# 261. Graph Valid Tree

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

'''

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