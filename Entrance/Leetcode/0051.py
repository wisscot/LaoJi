# 51. N-Queens

'''
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.
'''

Basic idea: DFS
Seach Template


class Solution:
    """
    @param: n: The number of queens
    @return: All distinct solutions
    """
    def solveNQueens(self, n):
        # write your code here
        
        res = []
        self.search(n, [], res)
        return res
        
    def search(self, n, path, res):
        
        if len(path) == n:
            self.save_result(path, res)
            
        for i in range(n):
            if not self.is_valid(path, i):
                continue
            
            path.append(i)
            self.search(n, path,res)
            path.pop()  # NOT pop(i)

    def is_valid(self, path, i):
        curr_row = len(path)
        curr_col = i
        for row, col in enumerate(path):
            if curr_col == col:
                return False
            if curr_col + curr_row == row + col:
                return False
            if curr_row - curr_col == row - col:
                return False
        return True
        
    def save_result(self, path, res):
        
        n = len(path)
        chess = []
        for col in path:
            line = ['.'] * n
            line[col] = 'Q'
            chess.append(''.join(line))
        
        res.append(chess)