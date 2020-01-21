# 97. Interleaving String

Basic idea: DP
we can use three dimentions i,j,k to track s1, s2, s3
if last char in s3 is the same as in s1 or s2, then we can remove that one and repeat

note that the length of s3 has to be the sum of s1 and s2,
we can remove one dimention k, as k always equals to i+j+1

base case:
if one string is empty, we check if other string == target

Time: O(mn)
Space: O(mn)  can reduce to O(n) using sliding array


# Solution 1: Recursive
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False
        
        import functools
        @functools.lru_cache(None)
        def dp(i,j):
            if i<0:
                return s2[:j+1] == s3[:j+1]
            if j<0:
                return s1[:i+1] == s3[:i+1]
            return (s1[i]==s3[i+j+1] and dp(i-1,j)) or (s2[j]==s3[i+j+1] and dp(i,j-1))       
        
        return dp(len(s1)-1, len(s2)-1)