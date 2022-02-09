# 623. K Edit Distance

'''
Given a set of strings which just has lower case letters and a target string, output all the strings for each the edit distance with the target no greater than k.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
Example
Example 1:

Given words = `["abc", "abd", "abcd", "adc"]` and target = `"ac"`, k = `1`
Return `["abc", "adc"]`
Input:
["abc", "abd", "abcd", "adc"]
"ac"
1
Output:
["abc","adc"]

Explanation:
"abc" remove "b"
"adc" remove "d"
Example 2:

Input:
["acc","abcd","ade","abbcd"]
"abc"
2
Output:
["acc","abcd","ade","abbcd"]

Explanation:
"acc" turns "c" into "b"
"abcd" remove "d"
"ade" turns "d" into "b" turns "e" into "c"
"abbcd" gets rid of "b" and "d"
'''

Basic idea:
DP + Trie + DFS

use T as the row of 2d transfer matrix T[i][j]
newT is the next row of T
this is the idea of DP sliding array

edge case: if words contains a empty string, it cannot be marked in Trie

class TrieNode:
    def __init__(self):
        self.word = ''
        self.char_child = collections.defaultdict(TrieNode)
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, word):
        node = self.root
        for char in word:
            node = node.char_child[char]
        node.word = word

class Solution:
    """
    @param words: a set of stirngs
    @param target: a target string
    @param k: An integer
    @return: output all the strings that meet the requirements
    """
    def kDistance(self, words, target, k):
        # write your code here
        
        # build trie
        trie = Trie()
        for word in words:
            trie.add(word)
            
        res = []
        # take care of edge case
        if '' in words and len(target)<=k:
            res.append('')

        T = list(range(len(target)+1)) #first row of T
        self.dfs(trie.root, target, T, k, res)

        return res
        
    def dfs(self, node, target, T, k, res):
        
        if node.word and T[len(target)]<=k: # T[len(target)] is the min distance between current node-word and target word
            res.append(node.word) # do not return as there maybe other word downwards the tree
        
        for char in node.char_child:
            newT = [0]*(len(target)+1)
            newT[0] = T[0] + 1
            for j in range(1, 1+len(target)):
                if target[j-1] == char:
                    newT[j] = T[j-1]
                else:
                    newT[j] = min(T[j-1], T[j], newT[j-1])+1
                    
            self.dfs(node.char_child[char], target, newT, k, res)
                
                
                
                
