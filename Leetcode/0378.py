# 378. Kth Smallest Element in a Sorted Matrix

'''
Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
'''


Basic idea:
get current smallest words, add its neighbor to a data stuctrue, then get minimum again, do this k times

Solution 1:
start from top left corner,
add it to heapq, 
heappop minimum then add its two neighbors
(need a set to check the neighbor has been visited or not)

Solution 2:
start from top line,
add them to heapq, 
heappop minimum then add the num pysically below it in the matrix if exists

Time both O(klogm)

Solution 3/4:
naive sort all O(mnlogmn)
QuickSelect O(mn)


# Solution 1
class Solution:
    def kthSmallest(self, matrix, k):
        # write your code here
        import heapq
        
        hq = [(val, 0, i) for i, val in enumerate(matrix[0])] # (val, row, col)
        heapq.heapify(hq)
        
        for _ in range(k):
            val, row, col = heapq.heappop(hq)
            if row == len(matrix)-1:
                continue
            heapq.heappush(hq, (matrix[row+1][col], row+1, col))
            
        return val


# Solution 2
class Solution:
    def kthSmallest(self, matrix, k):
        # write your code here
        import heapq
        di, dj = [1,0], [0,1]
        
        i = j = 0
        hq = [(matrix[i][j], i, j)]
        visited = set([(i, j)])
        
        rank = 0
        while rank < k:
            curr = heapq.heappop(hq)
            for dirc in range(2):
                _, i, j = curr
                i_, j_ = i+di[dirc], j+dj[dirc]
                if (i_, j_) in visited:
                    continue
                
                if i_ < len(matrix) and j_ < len(matrix[0]):
                    heapq.heappush(hq, (matrix[i_][j_], i_, j_))
                    visited.add((i_, j_))
            rank += 1
                    
        return curr[0]