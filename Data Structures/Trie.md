# Trie

## Overview 

Good for strings / words search which needs __words prefix__

> if there's no child, make child, if there's child, going down

## Template
```python
class TrieNode:
    def __init__(self):
        self.word = ''
        self.char_child = collections.defaultdict(TrieNode)
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def add(self, word):
        node = self.root
        # !!! easy to make mistake using node[char] = ...
        # !!! will rewrite the previous node
        for char in word:
            node = node.char_child[char]
        node.word = word
        
```

__Examples:__


[211. Add and Search Word - Data structure design](https://leetcode.com/problems/add-and-search-word-data-structure-design/)
wild card '.' needs dfs

[212. Word Search II](https://leetcode.com/problems/word-search-ii/)
difficult

[425. Word Squares](https://leetcode.com/problems/word-squares/)

TAG
[642. Design Search Autocomplete System](https://leetcode.com/problems/design-search-autocomplete-system/)
0208G