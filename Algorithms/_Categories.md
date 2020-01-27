# Sorting 

[912. Sort an Array](https://leetcode.com/problems/sort-an-array/)

## Quick Sort

Code1: easy to explain, use more space
```python
def quicksort(self, nums):
    if len(nums) <= 1:
        return nums

    pivot = random.choice(nums)
    lt = [v for v in nums if v < pivot]
    eq = [v for v in nums if v == pivot]
    gt = [v for v in nums if v > pivot]

    return self.quicksort(lt) + eq + self.quicksort(gt)
```

Code2: typical
Time: O(nlogn) Space:O(1)
```python
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quicksort(nums, 0, len(nums)-1)
        return nums
    
    def quicksort(self, nums, left, right):
    
        if left >= right:
            return 
        pivot = nums[right]
        # ssssssssbbbbbsbssbbbbp
        # l       j    i       r
        j = left  # Do NOT assign 0 to j
        for i in range(left, right): 
            if nums[i] < pivot:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
        nums[right], nums[j] = nums[j], nums[right] # not nums[-1]
        # sssssspbbbbbbbbb
        # l     j        r
        self.quicksort(nums, left, j-1)
        self.quicksort(nums, j+1, right)
```

## Merge Sort

## Bucket Sort ?

[164. Maximum Gap](https://leetcode.com/problems/maximum-gap/)

## Radix Sort ?

<br></br>

# Shortest Path in Graph

Type: weighted/unweighted, directed\
Note: directed graph is more general, we can code undirected graph to directed graph


__Exapmle:__

[1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance](https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/)

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
    
    # graph: {node:[(neighbor, edgeweight), ...]}
    hqueue = [(0, source)] # init priority queue [(dist, node), ...]
    dist = [float('inf')]*len(graph) # init dist from source
    dist[i] = 0
    
    while hqueue:
        # node can be added to hqueue mutiple times
        # need to process after pop 
        d, node = heapq.heappop(hqueue)
        if d > dist[node]: 
            continue
        
        for nb, w in graph[currnode]:
            if dist[nb] > d+w:
                dist[nb] = d+w
                heapq.heappush(hqueue, (d+w, nb))
```

Time: O(|E|log|E|)


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
            dist(i,j) = min{dist(i,k)+dist(k,j), dist(i,j)}
```
Time: O(|V|^3)

Negative weight cycle detect: if there is a negative weight cycle, then from some vertex to itself, it will be negative.  So we only need to check any(dist(u,u) ∀ u ∈ V) is negative.


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
