# 1057. Campus Bikes

'''
On a campus represented as a 2D grid, there are N workers and M bikes, with N <= M. Each worker and bike is a 2D coordinate on this grid.

Our goal is to assign a bike to each worker. Among the available bikes and workers, we choose the (worker, bike) pair with the shortest Manhattan distance between each other, and assign the bike to that worker. (If there are multiple (worker, bike) pairs with the same shortest Manhattan distance, we choose the pair with the smallest worker index; if there are multiple ways to do that, we choose the pair with the smallest bike index). We repeat this process until there are no available workers.

The Manhattan distance between two points p1 and p2 is Manhattan(p1, p2) = |p1.x - p2.x| + |p1.y - p2.y|.

Return a vector ans of length N, where ans[i] is the index (0-indexed) of the bike that the i-th worker is assigned to.
'''

Basic idea: Sort

Regular Sort or bucket sort, depending on the key value range


# Bucket Sort
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        buckets = [[] for _ in range(2001)]
        for worker, workerpos in enumerate(workers):
            for bike, bikepos in enumerate(bikes):
                d = abs(workerpos[0]-bikepos[0]) + abs(workerpos[1]-bikepos[1])
                buckets[d].append((worker, bike))
                
        visited_bike = set()
        visited_worker = set()
        
        res = [-1] * len(workers)
        for i in range(2001):
            buckets[i].sort()
            for worker, bike in buckets[i]:
                if worker in visited_worker or bike in visited_bike:
                    continue
                res[worker] = bike
                visited_worker.add(worker)
                visited_bike.add(bike)
            if len(visited_worker) == len(workers):
                break
        
        return res
        
            
            