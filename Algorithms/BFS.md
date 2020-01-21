# Breath First Search

## Templates

Template 1: No layer BFS
```python
queue = collections.deque([root])
visited = set([root])

while len(queue):
    head = queue.popleft()
    for neighbor in head.neighbors:
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)
```
Visited and Queue are always togeter


Template 2: Layer by layer BFS
```python
queue = collections.deque([root])
visited = set([root])

while queue:
    numlayer += 1
    for _ in range(len(queue)):
        head = queue.popleft()
        for neighbor in head.neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
```


Prefer BFS over DFS 

__Applications:__
* Tree search by layer
* Coonected components (alternative UnionFind)
* Find shortest path in graph (simple graph)
* Topological sort (directed graph)

__Examples:__

[297. Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/)
\
BFS is one way to serialize and deserialize 

[133. Clone Graph](https://leetcode.com/problems/clone-graph/)
\
BFS to get all connected nodes

[127. Word Ladder](https://leetcode.com/problems/word-ladder/)
\
Shorest Path

[207. Course Schedule](https://leetcode.com/problems/course-schedule/)\
[210. Course Schedule II](https://leetcode.com/problems/course-schedule-ii/)
\
Topo sort

[269. Alien Dictionary](https://leetcode.com/problems/alien-dictionary/)
\
Topo sort
