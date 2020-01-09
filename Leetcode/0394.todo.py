# 394. Decode String

'''
Basic idea:
Solution 1. Recursive
Solution 2. Iterative
  use stack to save the charactors in the string
  if closing bracket meet, then assemble the latest words before it
  e.g. abc3[ef]
  Step 1. stack -> 'a', 'b', 'c', '3', '[', 'e', 'f'
  Step 2. pop out 'e' and 'f', save it
  Step 3. get the number before '['
  Step 4. assemble 'ef'*3 and save back to stack

Time: O(n)
'''

class Solution:
    """
    @param s: an expression includes numbers, letters and brackets
    @return: a string
    """
    def expressionExpand(self, s):
        stack = []
        for c in s:
            if c != ']':
                stack.append(c)
                continue
            
            curr = []
            while stack[-1] != '[':
                curr.append(stack.pop())
                
            stack.pop()
            
            num = 0
            base = 1
            while stack and stack[-1].isdigit():
                num += int(stack.pop())*base
                base *= 10
            
            stack.append(''.join(curr[::-1])*num)
            
        return ''.join(stack)
            
            
