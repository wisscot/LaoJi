# 42. Trapping Rain Water

'''
Basic idea:
1D version of the trapping water
Solution 1:
  similar to 1D version, get max out from boundary with heap, which only contains two elements
Solution 2:
  use two pointers to track, similar to above, but more concise
Solution 3:
  for every cell, the water contain capability decided by the min(max num to the left, max num to the right)
  which leads to mono stack naturally

- solution 2 is preferred
  
Time O(n)
'''

# Not a good solution, do it again
# check out solution from lintcode
class Solution:
    """
    @param heights: a list of integers
    @return: a integer
    """
    def trapRainWater(self, heights):
        # write your code here
        if not heights:
            return 0 
        
        waterlevels = list(heights)
        visited = [False]*len(heights)
        
        walls = [(heights[0],0),(heights[-1],len(heights)-1)]  # (height, index)
        visited[0] = visited[-1] = True
        
        while walls:
            walls.sort()
            lowwall = walls.pop(0)
            h, i = lowwall      
            for di in [-1,1]:
                i_ = i+di
                if i_ < 0 or i_ >= len(heights) or visited[i_]:
                    continue
                waterlevels[i_] = max(h, heights[i_])
                walls.append((waterlevels[i_], i_))
                visited[i_] = True
                
        return sum(waterlevels[i] - heights[i] for i in range(len(heights)))
                
        
            
