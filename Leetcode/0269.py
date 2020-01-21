# 269. Alien Dictionary

'''
There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

Example 1:

Input:
[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]

Output: "wertf"
'''

Basic idea:
build a graph G = (V, E), where V is the character and E is the directed edge
Then topo sort

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # Write your code here
        
        # build the graph
        node_children = {char:set() for word in words for char in word}
        for i in range(len(words)-1):
            self.buildedges(node_children, words[i], words[i+1])
        indegree = {node:0 for node in node_children}
        for node in node_children:
            for child in node_children[node]:
                indegree[child] += 1
                
        # topo sort
        queue = collections.deque()
        for node in indegree:
            if indegree[node] == 0:
                queue.append(node)
        
        res = []
        while queue:
            head = queue.popleft()
            res.append(head)
            for node in node_children[head]:
                indegree[node] -= 1
                if indegree[node] == 0:
                    queue.append(node)
        
        for node in indegree:
            if indegree[node] > 0:
                return ''
                
        return ''.join(res)
            
    def buildedges(self, node_children, word1, word2):
        for i in range(min(len(word1), len(word2))):
            if word1[i] == word2[i]:
                continue
            node_children[word1[i]].add(word2[i])
            return
                