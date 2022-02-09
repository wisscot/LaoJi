# 150. Evaluate Reverse Polish Notation

'''
Basic idea:
stack to store the result
'''

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for token in tokens:
            if token[-1].isdigit(): # cannot use token.isdigit() for negative num
                stack.append(int(token))
                continue
                
            num2 = stack.pop()   # num1, num2 position matters
            num1 = stack.pop()
            if token == '+':
                stack.append(num1+num2)  
            if token == '-':
                stack.append(num1-num2)
            if token == '*':
                stack.append(num1*num2)
            if token == '/':
                stack.append(int(num1/num2))
            
        return stack[-1]