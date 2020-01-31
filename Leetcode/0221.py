# 221. Maximal Square

'''
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
'''

Basic idea: DP

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = int(matrix[i][j])
                
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    continue
                matrix[i][j] = max(matrix[i][j], 
                                   1 + min(matrix[i-1][j-1],
                                           matrix[i-1][j],
                                           matrix[i][j-1])
                                  )
                
        side = max(max(matrix[i]) for i in range(len(matrix)))
        return side**2
