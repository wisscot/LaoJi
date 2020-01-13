3. Longest Substring Without Repeating Characters

Basic idea:
1. move j until cannot
2. save result
3. move i


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        j = 0
        curr_letters = set()
        
        # master pointer use for loop
        for i in range(len(s)):
            # slave pointer use while loop
            # move j until cannot
            while j < len(s) and s[j] not in curr_letters:
                curr_letters.add(s[j])
                j += 1
            # save result
            res = max(res, j-i)
            # move i
            curr_letters.remove(s[i])
            
        return res        
