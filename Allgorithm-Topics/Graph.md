# Shortest Path in Graph

Type: weighted/unweighted, directed\
Note: directed graph is more general, we can code undirected graph to directed graph

__Exapmle:__

[1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance](https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/)

TAG
[743. Network Delay Time](https://leetcode.com/problems/network-delay-time/)
\
Dijkstra's Algorithm

## BFS

No weight on edge (w(e)=1 ∀ e ∈ E)

see BFS part

Time: O(|E|)

## Dijkstra

Positive weighted edge

Get distances from one vertex to all other vertices

If there is a negative cycle, Dijkstra algo will go into inf loop

```python
# Step 1. assign inf dist to all other nodes, and save source node to heapq
# Step 2. heappop the current closest one, check if already visited by dist
# Step 3. add neighbor to heapq if new dist is shorter
def dijkstra(self, graph, source):
    
    # graph -> {node:[(neighbor, edgeweight), ...]}
    
    hqueue = [(0, source)] # init priority queue [(dist, node), ...]
    
    node_dist = {} # save finalized (minimum dist) nodes here
    
    while hqueue:
        # node can be added to hqueue mutiple times
        # need to process after pop 
        d, node = heapq.heappop(hqueue)
        if node in node_dist: 
            continue
        node_dist[node] = d

        for nb, w in graph[currnode]:
            if nb in node_dist:
                continue
            heapq.heappush(hqueue, (d+w, nb))
```
Time: O(|E|log|E|)

## Bellman-Ford

Same functionality as Disjtra's Algorithm \
Pros: good with / can detect negative cycle

```python
# Step 1. assign 0, inf dist to source and other nodes
# Step 2. loop |V| - 1 times: for all edges (u,v): update_vertex_dist(v)
```
Time: O(|V|*|E|)

Negative cycle detect: run loop one more time, see if results remains the same

## Floyd-Warshall 

Weight on edge

Get distances from all vertices to all vertices

Basic idea: DP\
D(i,s,t) denotes shortest distance from s to t that can pass 1,2,...,i nodes. 

D(i,s,t) = min( D(i-1,s,t), D(i-1,s,i)+D(i-1,i,t)) \
either pass vertex i or not pass i

Base Case: \
D(0,u,u) = 0\
D(0,u,v) = w(u,v) ∀ known edges \
D(0,u,v) = ∞ ∀ all other edges 

we can reduce the 'i' dimension to save space:\
D(s,t) = min( D(s,t), D(s,i)+D(i,t))

Assumption: no negative weight cycle

```python
# pseudo code
# Step 1. assign dist pairs to adjacent matrix
# Step 2. loop all pairs using mid point

# initiation adjacent matrix
for i=1 to n: 
    for j = 1 to n:
        dist(i, j) = ∞ 
for all (i, j) ∈ E:
    dist(i, j) = l(i, j) 
    
# DP iterations
for k = 1 to n:
    for i=1 to n: 
        for j = 1 to n:
            dist(i,j) = min{dist(i,j), dist(i,k)+dist(k,j)}
```
Time: O(|V|^3)

Negative weight cycle detect: if there is a negative weight cycle, then from some vertex to itself, it will be negative.  So we only need to check any(dist(u,u) ∀ u ∈ V) is negative.

# Minimum weight of Graph
## Minimum Spanning Tree (MST)

Undirected graph only

Two Algo.
 * Kruskal
 * Prim
 
```python
# Kruskal's Algorithm
# pseudo code

# Step 1. sort edges
# Step 2. check edge from smallest
# Step 3. add edge to result if two node not connected, and union them, repeat

Input: G = (V,E), weights w(e)

res = []
for e{u,v} in sorted E: # greedy
    if find(u) != find(v): # UnionFind
        add edge e{u,v} to res
        union(u,v)
        
return(res)
```
Time Complexity:  O(|E|log|E|)



# Graph

TAG
[1153. String Transforms Into Another String](https://leetcode.com/problems/string-transforms-into-another-string/)
\
Interesting problem