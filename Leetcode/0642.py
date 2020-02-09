# 642. Design Search Autocomplete System

Implement Trie


class TrieNode:
    def __init__(self):
        self.cntword = None
        self.char_child = collections.defaultdict(TrieNode)
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def add(self, word, cnt):
        node = self.root
        for char in word:
            node = node.char_child[char]
        node.cntword = [cnt, word]

class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.trie = Trie()
        for sentence, cnt in zip(sentences, times):
            self.trie.add(sentence, cnt)
        
        self.node = self.trie.root
        self.chars = []

    def input(self, c: str) -> List[str]:
        if c == '#':
            if self.node.cntword:
                self.node.cntword[0] += 1
            else:
                self.node.cntword = [1, ''.join(self.chars)]
                
            self.node = self.trie.root
            self.chars = []
            return
        
        self.node = self.node.char_child[c]
        self.chars.append(c)
        res = []
        self.search(self.node, res)
        
        return [sentence for _, sentence in sorted(res, key=lambda x:(-x[0],x[1]))[:3]]
        
    def search(self, curr, res):
        if curr.cntword:
            res.append(curr.cntword)
            
        for child in curr.char_child.values():
            self.search(child, res)
    
