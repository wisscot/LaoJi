# 10. String Permutation II

'''
Given a string, find all permutations of it without duplicates.
Example 1:

Input: "abb"
Output:
["abb", "bab", "bba"]
'''

Basic idea: DFS
be cautious for identical characters, 
if previous one has not been visited, 
then the current one should not be included.
otherwise, there will be duplicates

class Solution:
    """
    @param str: A string
    @return: all permutations
    """
    def stringPermutation2(self, str):
        # write your code here
        
        res = []
        s = sorted(list(str))
        visited = [False] * len(s)
        self.search(s, visited, [], res)
        
        return res
        
    def search(self, s, visited, path, res):
        
        if len(path) == len(s):
            res.append(''.join(path))
            return
        
        for i in range(len(s)):
            if visited[i]:
                continue
            
            if i and s[i] == s[i-1] and not visited[i-1]:
                continue
            
            path.append(s[i])
            visited[i] = True
            
            self.search(s, visited, path, res)
            
            path.pop()
            visited[i] = False