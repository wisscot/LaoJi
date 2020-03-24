# 125. Valid Palindrome

'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.
'''

Solution 1: check preprocessed s == s[::-1]
Space: O(n)

Solution 2: two pointers
Space: O(1)

# Solution 1:
class Solution:
    def isPalindrome(self, s):        
        s = ''.join([char.lower() for char in s if char.isalnum()])
        return s == s[::-1]

# Solution 2
class Solution:
    def isPalindrome(self, s):        
        left, right = 0, len(s)-1
        while left < right:
            while left<right and not s[left].isalnum():
                left += 1
            
            while left<right and not s[right].isalnum():
                right -= 1
                
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
            
        return True