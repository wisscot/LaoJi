# 394. Decode String

'''
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
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


# Iterative with stack
class Solution:
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
            
            
