# 47. Permutations II

'''
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
'''

Basic idea: DFS
be cautious for identical characters, 
if previous one has not been visited, 
then the current one should not be included.
otherwise, there will be duplicates

Solution 1: every node will sweep the whole array,
So we do NOT need previous node index status

Solution 2: using count, sweep the key in the count

# Solution 1
class Solution:
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


# Solution 2: count
class Solution:
    def stringPermutation2(self, str):
        # write your code here
        count = collections.Counter(str)
        res = []
        self.search(len(str), count, [], res)
        return res
        
    def search(self, n, count, path, res):
        if len(path) == n:
            res.append(''.join(path))
            
        for char in count:
            if count[char] == 0:
                continue
            count[char] -= 1
            path.append(char)
            self.search(n, count, path, res)
            path.pop()
            count[char] += 1
