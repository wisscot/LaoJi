# 127. Word Ladder

Basic idea:
typical BFS, find the shorest path


class Solution:
    def ladderLength(self, start, end, words):
        # write your code here
        words.add(end)

        # build word patterns mapping
        pattern_words = self.buildpattern(words)
        
        res = 0
        queue = collections.deque([start])
        visited = set([start])
        
        # BFS find shortest path
        while queue:
            res += 1
            for _ in range(len(queue)):
                head = queue.popleft()
                if head == end:
                    return res
                neighbors = self.getneighbors(head, pattern_words)
                for nb in neighbors:
                    if nb in visited:
                        continue
                    queue.append(nb)
                    visited.add(nb)
                    
        return 0
                    
    def buildpattern(self, words):
        p_words = collections.defaultdict(list)
        for word in words:
            for p in self.patterns(word):
                p_words[p].append(word)
        return p_words
        
    def patterns(self, word):
        patts = []
        for i in range(len(word)):
            patts.append(word[:i]+'_'+word[i+1:])
        return patts
        
    def getneighbors(self, word, p_words):
        neighbors = []
        for patt in self.patterns(word):
            neighbors += p_words[patt]
        return set(neighbors)
            
        
        
        
        