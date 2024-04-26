# Breath First Search

## Summary

queue 和 visited 是一对好基友，总是同时出现

## Templates

Template 1: No layer BFS
```python
queue = collections.deque([root])
visited = set([root])

while len(queue):
    head = queue.popleft()
    for neighbor in head.neighbors:
        if neighbor not in visited:
            queue.append(neighbor)
            visited.add(neighbor)
```

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
                queue.append(neighbor)
                visited.add(neighbor)
```

## Applications
* Tree search by layer
* Connected components (alternative UnionFind)
* Find shortest path in graph (simple graph)
* Topological sort (directed graph)

Prefer BFS over DFS 

__Examples:__

[133. Clone Graph](https://leetcode.com/problems/clone-graph/)
Medium 2020 2024
BFS to get all connected nodes

[127. Word Ladder](https://leetcode.com/problems/word-ladder/)
Hard 2020, 2024
Shorest Path

Topo sort
[207. Course Schedule](https://leetcode.com/problems/course-schedule/)
Medium 2020, 2024
[210. Course Schedule II](https://leetcode.com/problems/course-schedule-ii/)
Medium 2020, 2024

Topo sort
[269. Alien Dictionary](https://leetcode.com/problems/alien-dictionary/)
Premium 2020 

[752. Open the Lock](https://leetcode.com/problems/open-the-lock/)
Medium 2020 2024

[297. Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/)
Hard 2020 2024
BFS or preorder DFS with iterator

TAG
[1197. Minimum Knight Moves](https://leetcode.com/problems/minimum-knight-moves/)