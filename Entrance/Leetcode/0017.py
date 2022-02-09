# 17. Letter Combinations of a Phone Number

'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
'''

Basic idea: DFS

Easy backtracking


KEYBOARD = ['', '', 'abc', 'def','ghi', 'jkl', 'mno', 'pqrs','tuv','wxyz']

# KEYBOARD[I] -> letter

class Solution:
    """
    @param digits: A digital string
    @return: all posible letter combinations
    """
    def letterCombinations(self, digits):
        # write your code here
        
        if not digits:
            return []
        
        res = []
        self.search(digits, 0, [], res)
        return res
        
    def search(self, digits, idx, path, res):
        if idx == len(digits):
            res.append(''.join(path))
            return
            
        for char in KEYBOARD[int(digits[idx])]:
            path.append(char)
            self.search(digits, idx+1, path, res)
            path.pop()
