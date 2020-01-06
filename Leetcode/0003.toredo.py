Basic idea:
1. move j until cannot
2. save result
3. move i


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        j = 0
        curr_letters = set()
        
        for i in range(len(s)):
            while j < len(s) and s[j] not in curr_letters:
                curr_letters.add(s[j])
                j += 1
            
            res = max(res, j-i)
            curr_letters.remove(s[i])
            
        return res        
