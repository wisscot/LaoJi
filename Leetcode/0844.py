# 844. Backspace String Compare

'''
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
'''

Solution 1: stack
Time O(n) Space O(n)

Solution 2: two pointers
Time O(n) Space O(1)

Solution 2+: generator
Time O(n) Space O(1)


# Solution 2+
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        
        genS = self.gen(S)
        genT = self.gen(T)
        char1, char2 = next(genS,None), next(genT,None)
        while char1 == char2 and char1 is not None:
            char1, char2 = next(genS,None), next(genT,None)
            
        return char1 == char2
    
    def gen(self, s):
        skip = 0
        for char in reversed(s):
            if char == '#':
                skip += 1
            elif skip:
                skip -= 1
            else:
                yield char
                

            
        