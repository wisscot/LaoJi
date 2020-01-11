# 227. Basic Calculator II

'''
Basic idea:
scan the expression from left to right
store number and previous operation
use a stack to 
'''


class Solution:
    def calculate(self, s: str) -> int:
        num = 0
        prevop = '+'
        stack = []
        
        # last char is a digit, without this last num does not go to stack
        s += '#' 
        
        i = 0
        while i < len(s):
            char = s[i]
            if char == ' ':
                i += 1 # be caution to add this with "while" and "continue"
                continue
            if char.isdigit():
                num = num*10 + int(char)
                i += 1
                continue

            # if current char is operator, 
            # check previous operator's status
            if prevop == '+':
                stack.append(num)
            elif prevop == '-':
                stack.append(-num)
            elif prevop == '*':
                stack.append(stack.pop()*num)
            elif prevop == '/':
                stack.append(int(stack.pop()/num))
                            
            num = 0
            prevop = char
            i += 1
            
        return sum(stack)        