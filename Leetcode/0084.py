# 84. Largest Rectangle in Histogram

'''
Basic idea:
  1. get all possible large rectangle
  2. every possible large rectangle will reach one of the tops
  3. so the idea is to get every possible rectangle according to every top
  4. for each top, find left and right first lower top than current, area=height*(right-left-1)
  5. Monotonous Stack can be used for this purpose

Time O(n)
'''

class Solution:
    """
    @param height: A list of integer
    @return: The area of largest rectangle in the histogram
    """
    def largestRectangleArea(self, height):
        # write your code here
        res = 0

        monostack = [(0,-1)] #height, index
        for i, h in enumerate(height+[0]):
            while h < monostack[-1][0]:
                prev_h, _ = monostack.pop()
                res = max(res, prev_h*(i-monostack[-1][1]-1))
            monostack.append((h,i))

        return res