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

# Solution: Two pointers
class Solution:
    def trap(self, height: List[int]) -> int:
        waterlevel = list(height)
        
        i, j = 0, len(height) - 1
        while i < j - 1:
            if height[i] <= height[j]:
                waterlevel[i+1] = max(waterlevel[i+1], waterlevel[i])
                i += 1
            else:
                waterlevel[j-1] = max(waterlevel[j-1], waterlevel[j])
                j -= 1
                
        return sum(waterlevel[i]-height[i] for i in range(len(height)))
        
                
        
            
