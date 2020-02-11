# 85. Maximal Rectangle

'''
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.
'''

Basic idea:
Count how many continus ones at and above current position
for each row, this problem convert to Largest_Rectangle_in_Histogram problem (Leetcode 84).


class Solution:
    """
    @param matrix: a boolean 2D matrix
    @return: an integer
    """
    def maximalRectangle(self, matrix):
        # write your code here
        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1 and matrix[i-1][j] > 0:
                    matrix[i][j] += matrix[i-1][j]
            
        res = 0        
        for i in range(len(matrix)):
            res = max(res, self.Largest_Rectangle_in_Histogram(matrix[i]))

        return res
        
    def Largest_Rectangle_in_Histogram(self, heights):
        monostack = [(-1, 0)]
        res = 0
        for i, h in enumerate(heights+[0]):
            while h < monostack[-1][1]:
                _, currh = monostack.pop()
                res = max(res, currh*(i-monostack[-1][0]-1))
            monostack.append((i,h))
        return res
        
    
            
