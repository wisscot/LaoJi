# 91. Decode Ways

'''
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
'''

Basic idea:
Typical DP
specially deal with first character


class Solution:
    """
    @param s: a string,  encoded message
    @return: an integer, the number of ways decoding
    """
    def numDecodings(self, s):
        # write your code here
        if not s or s[0] == '0':
            return 0
            
        T = [1] * (len(s)+1)
        
        for i in range(1, len(s)):
            T[i+1] = T[i]*(int(s[i])>0) + T[i-1]*(10<=int(s[i-1:i+1])<=26)
                                                  ^
                        #  in this problem '02' can not be translated to '2', so...
            if T[i+1] == 0:
                return 0
                
        return T[-1]
