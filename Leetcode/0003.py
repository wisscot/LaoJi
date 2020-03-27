# 3. Longest Substring Without Repeating Characters

Basic idea: Two pointers (Onwards)

Solution 1:
Master on right, slave on left

Solution 2:
Master on left, slave on right


# Solution 1
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        window = set()
        
        # ... | 1 3 4 | 2 3 4
        #       i   j
        i = 0
        for j in range(len(s)):
            while s[j] in window:
                window.remove(s[i])
                i += 1
            res = max(res, j - i + 1)
            
            window.add(s[j])
            
        return res

# Solution 2
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
