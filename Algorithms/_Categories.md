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



<br></br>

# Shortest Path in Graph

[1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance](https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/)

## BFS

No weight on edge, directed or undirected

see BFS part

Time: O(|E|)

## Dijkstra

Weight on edge, directed or undirected

Get distances from one vertex to all other vertices

```python
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
            nbdist = d + w
            if nbdist < dist[nb]:
                dist[nb] = nbdist
                heapq.heappush(hqueue, (currdist+w, nb))
```

Time: O(|E|log|E|)


## Floyd-Warshall 

Weight on edge, directed or undirected

Get distances from all vertices to all vertices

Basic idea: DP

```python
# pseudo code
for i=1 to n: 
    for j = 1 to n:
        dist(i, j) = ∞ # initiation
for all (i, j) ∈ E:
    dist(i, j) = l(i, j) # initiation
for k = 1 to n:
    for i=1 to n: 
        for j = 1 to n:
            dist(i,j) = min{dist(i,k)+dist(k,j), dist(i,j)}
```
Time: O(|V|^3)