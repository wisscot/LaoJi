# 680. Valid Palindrome II

'''
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
'''

Basic idea:
when encounter different chars, check if leftover isPalindrome after removal

class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left<right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return self.isPalin(s, left+1, right) or self.isPalin(s, left, right-1)
            
        return True
    
    def isPalin(self, s, i, j): # can be improved by two pointers
        s_new = s[i:j+1]
        return s_new == s_new[::-1]