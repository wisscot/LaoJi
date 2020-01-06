# 159. Longest Substring with At Most Two Distinct Characters
Two pointers
Be careful with the slave pointer j stop condition


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        res = 0
        k = 2
        
        count = collections.Counter()
        j = 0
        # |a b c e e a i w|
        #  ^               ^
        #  i               j
        # len = j - i
        for i in range(len(s)):
            while j < len(s) and self.can_add(s[j], count, k):
                count[s[j]] += 1
                j += 1
                
            res = max(res, j-i)
                
            count[s[i]] -= 1
            if count[s[i]] == 0:
                count.pop(s[i])
                
        return res
            
    def can_add(self, char, count, k):
        if char in count:
            return len(count) <= k
        return len(count)+1 <= k        
