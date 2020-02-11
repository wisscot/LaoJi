# 973. K Closest Points to Origin

'''
We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)
'''

Solution 0: Brute Force, Find max, remove, repeat
Time O(nk)

Solution 1: Sort and get first K (offline)
Time O(nlogn + K)

Solution 2: Min heap and get first K (offline)
Time O(n + Klogn)
Time O(nlogn)    (online)

Solution 3: Max heap (len==k) and get all (online)
Time O(nlogK)

Solution 4: quick select, find kth, then loop once, sort (Offline)
Time O(n + KlogK)


# Solution 2
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        
        hqueue = [] # min heap
        for point in points:
            x, y = point
            dist = (x**2 + y**2)**0.5
            heapq.heappush(hqueue, (dist, point))
        
        res = []
        for _ in range(K):
            res.append(heapq.heappop(hqueue)[1])
            
        return res
        