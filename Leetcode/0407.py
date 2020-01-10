# 407. Trapping Rain Water II

'''
Basic idea:
Water barral principle: water capacity of a water barral depends on the shortest board.
Starting from the boarder of the matrix, those water level can be fixed (itself)
find the shortest one,
then the neighbors of this one can be acquired by comparing the height and current level:
if height[neighbor] <= current_level:
    waterlevel[neighbor] = current_level
if height[neighbor] > current_level:
    waterlevel[neighbor] = height[neighbor]

Time O(mnlogmn)
'''


class Solution:
    """
    @param heights: a matrix of integers
    @return: an integer
    """
    def trapRainWater(self, heights):
        # write your code here
        import heapq
        if not heights:
            return 0
            
        waterlevel = [['#']*len(heights[0]) for _ in range(len(heights))]
        hp = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if i==0 or j==0 or i==len(heights)-1 or j==len(heights[0])-1:
                    waterlevel[i][j] = heights[i][j]
                    heapq.heappush(hp, (waterlevel[i][j], i, j))
        
        directions = [(1,0),(-1,0),(0,1),(0,-1)]   
        while hp:
            currLowest, i, j = heapq.heappop(hp)
            for di, dj in directions:
                i_ = i + di
                j_ = j + dj
                if not self.with_in(heights, i_, j_) or waterlevel[i_][j_] != '#':
                    continue
                if heights[i_][j_] >= currLowest:
                    waterlevel[i_][j_] = heights[i_][j_]
                else:
                    waterlevel[i_][j_] = currLowest
                heapq.heappush(hp, (waterlevel[i_][j_], i_, j_))
                    
        res = 0
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                res += waterlevel[i][j] - heights[i][j]
                
        return res
        
    def with_in(self, heights, i, j):
        return 0<=i<len(heights) and 0<=j<len(heights[0])
            
                    
        
