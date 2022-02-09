# 22. Generate Parentheses

'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
For example, given n = 3, a solution set is:
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''

Basic idea: DFS

assume n == 2:
                     L=0, R=0
              '('/               \ 
             L=1, R=0             X
        '('/          \')'
      L=2, R=0        L=1, R=1        
      /     \')'       /    \
     X     L=2,R=1    ..     X        
          /       \')'
         X        L=2, R=2 (path=['(' '(' ')' ')'])  

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        self.search(n, 0, 0, [], res)
        return res
    
    def search(self, n, L, R, path, res):
        if R == n:
            res.append(''.join(path))
            return
        
        if L < n:
            path.append('(')
            self.search(n, L+1, R, path, res)
            path.pop()
        
        if L > R:
            path.append(')')
            self.search(n, L, R+1, path, res)
            path.pop()
            