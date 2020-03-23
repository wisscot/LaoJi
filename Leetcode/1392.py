# 1392. Longest Happy Prefix

'''
A string is called a happy prefix if is a non-empty prefix which is also a suffix (excluding itself).

Given a string s. Return the longest happy prefix of s .

Return an empty string if no such prefix exists.

Example 1:

Input: s = "level"
Output: "l"
Explanation: s contains 4 prefix excluding itself ("l", "le", "lev", "leve"), and suffix ("l", "el", "vel", "evel"). The largest prefix which is also suffix is given by "l".
'''


Basic idea: hash
Similar to Rabin-Karp algorithm


class Solution:
    def longestPrefix(self, s: str) -> str:
        l, r = 0, 0
        mod = 10**6 + 3
        res = ''
        for i in range(len(s)-1):
            l = (l*33 + ord(s[i])) % mod
            r = (r + pow(33, i, mod)*ord(s[~i])) % mod
            if l == r:
                res = s[:i+1]
        
        return res