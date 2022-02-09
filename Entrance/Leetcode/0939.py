# 939. Minimum Area Rectangle

'''
Given a set of points in the xy-plane, determine the minimum area of a rectangle formed from these points, with sides parallel to the x and y axes.

If there isn't any rectangle, return 0.
'''

Basic idea:
two nested loop find two corners,
use hashmap to find if the other two exist or not

Time O(n^2)

class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        
        existed = set((x, y) for x, y in points)
        
        res = float('inf')
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                if x1 == x2 or y1 == y2:
                    continue
                if (x1, y2) in existed and (x2, y1) in existed:
                    area = abs(y2-y1) * abs(x2-x1)
                    res = min(res, area)
                    
        return res if res<float('inf') else 0