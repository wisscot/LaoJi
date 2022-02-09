# 126. Word Ladder II

'''
Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return an empty list if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]
'''

Basic idea: BFS + DFS
Sortest -> BFS
Find all solution -> DFS

Step 1

class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: a list of lists of string
    """
    def findLadders(self, start, end, dict):
        # write your code here
        
        dict |= set([start, end])
        
        word_neibs = self.build_graph(dict) #graph builder O(|V| + |E|)
        
        word_dist = self.find_dist(end, start, word_neibs) # BFS O(|V| + |E|)
        
        res = []
        self.search(word_neibs, word_dist, start, end, [], res) # DFS le O(|V| + |E|)
        return res
        
    def build_graph(self, words):
        # return {word: [neighbors]}
        
        pattern_words = collections.defaultdict(set)
        for word in words:
            for i in range(len(word)):
                pattern = word[:i] + '_' + word[i+1:]
                pattern_words[pattern].add(word)
        
        word_neibs = collections.defaultdict(set)
        for word in words:
            for i in range(len(word)):
                pattern = word[:i] + '_' + word[i+1:]
                word_neibs[word] |= pattern_words[pattern]
        
        return word_neibs
            
    def find_dist(self, start, end, word_neibs):
        
        word_dist = {}
        
        queue = collections.deque([start])
        visited = set([start])
        
        dist = -1
        while queue:
            dist += 1
            for _ in range(len(queue)):
                word = queue.popleft()
                word_dist[word] = dist 
                # optional optimization TODO
                for neib in word_neibs[word]:
                    if neib in visited:
                        continue
                    queue.append(neib)
                    visited.add(neib)
            
        return word_dist
        
    def search(self, word_neibs, word_dist, start, end, path, res):
        
        if start == end:
            path.append(start)
            res.append(list(path))
            path.pop()
            return
        
        path.append(start)
        for neib in word_neibs[start]:
            if word_dist[start] != word_dist[neib] + 1:
                continue
            self.search(word_neibs, word_dist, neib, end, path, res)
        path.pop()
            
