# Breath First Search

## 

Template 1: No layer BFS
```python
from collections import deque
queue = deque()
seen = set()  #等价于Java版本中的set
seen.add(start)
queue.append(start)
while len(queue):
    head = queue.popleft()
    for neighbor in head.neighbors:
        if neighbor not in seen:
            seen.add(neighbor)
            queue.append(neighbor)
```
Seen and Queue are always togeter


Template 2: Layer by layer BFS
```python
queue = collections.deque([root])
seen = set([root])

while queue:
    for _ in range(len(queue)):
        head = queue.popleft()
        for neighbor in head.neighbors:
            if neighbor not in seen:
                seen.add(neighbor)
                queue.append(neighbor)
```