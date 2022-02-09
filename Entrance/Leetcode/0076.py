76. Minimum Window Substring

Basic idea:
use two pointers and Counter to count all the element inside the window,
use another variable to keep track how many char completed

Time O(n)

# Solution 1: master on left
class Solution:
    """
    @param source : A string
    @param target: A string
    @return: A string denote the minimum window, return "" if there is no such a string
    """
    def minWindow(self, source , target):
        # write your code here
        target_count = collections.Counter(target)
        curr_count = collections.Counter()
        
        res = ''
        j = 0
        numComp = 0
        min_len = len(source) + 1
        
        for i in range(len(source)):
            while j < len(source) and numComp < len(target_count):
                if source[j] in target_count:
                    curr_count[source[j]] += 1
                    if curr_count[source[j]] == target_count[source[j]]:
                        numComp += 1
                j += 1
                
            if numComp==len(target_count) and j - i < min_len:
                min_len = j - i
                res = source[i:j]
                
            if source[i] in target_count:
                curr_count[source[i]] -= 1
                if curr_count[source[i]] < target_count[source[i]]:
                    numComp -= 1
            
        return res
        

# Solution 2: master on right
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t = collections.Counter(t)
        count_s = collections.Counter()
        missing = len(t)
        
        i = 0
        min_len = float('inf')
        res = ''
        # a b c d e g a b c d
        # i     j
        for j in range(len(s)):
            count_s[s[j]] += 1
            if count_s[s[j]] <= count_t[s[j]]:
                missing -= 1
            
            while not missing:
                if j - i + 1 < min_len:
                    min_len = j - i + 1
                    res = s[i:j+1]
                    
                count_s[s[i]] -= 1
                if count_s[s[i]] < count_t[s[i]]:
                    missing += 1
                    
                i += 1
    
        return res