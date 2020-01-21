# 133. Clone Graph

'''
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
'''

Basic idea:
Step 1: Clone nodes (BFS)
Step 2: Clone edges

class Solution:
    """
    @param node: A undirected graph node
    @return: A undirected graph node
    """
    def cloneGraph(self, node):
        # write your code here
        if not node: return None
        
        oldnodes = self.getnodes(node)
        newnodes = []
        old_new = {}
        # clone vertices and create mapping
        for oldnode in oldnodes:
            newnode = UndirectedGraphNode(oldnode.label)
            old_new[oldnode] = newnode
            newnodes.append(newnode)
            
        # clone edges
        for oldnode in oldnodes:
            newnode = old_new[oldnode]
            newnode.neighbors = [old_new[nb] for nb in oldnode.neighbors]
            
        return old_new[node]
        
    def getnodes(self, node):
        # BFS to get all nodes connected
        res = []
        queue = collections.deque([node])
        visited = set([node])
        
        while queue:
            head = queue.popleft()
            res.append(head)
            for nb in head.neighbors:
                if nb in visited:
                    continue
                queue.append(nb)
                visited.add(nb)
                
        return res
