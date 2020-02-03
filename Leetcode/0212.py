# 212. Word Search II

'''
Given a 2D board and a list of words from the dictionary, find all words in the board.Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

Example:
Input: 
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
 
Note:
All inputs are consist of lowercase letters a-z.
The values of words are distinct.
'''

Basic idea: DFS + Trie
cannot visit already visited node in a deeper search

(Good one to practice)

class TrieNode:
    def __init__(self):
        self.word = '' # assume empty word is not valid
        self.char_child = collections.defaultdict(TrieNode)
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def add(self, word):
        node = self.root
        for char in word:
            node = node.char_child[char]
        node.word = word
        

DIRECTIONS = [(0,1), (1,0), (0,-1), (-1,0)]
class Solution:
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string
    """
    def wordSearchII(self, board, words):
        # write your code here
        
        trie = Trie()
        for word in words:
            trie.add(word)
            
        res = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.search(board, i, j, trie.root, res)
        return res
        
    def search(self, board, curr_row, curr_col, node, res):
        
        curr_char = board[curr_row][curr_col]
        if curr_char not in node.char_child: # include '#'
            return 
        
        if node.char_child[curr_char].word:
            res.append(node.char_child[curr_char].word)
            node.char_child[curr_char].word = ''
            
        board[curr_row][curr_col] = '#'
        for dx, dy in DIRECTIONS:
            new_row = curr_row + dx
            new_col = curr_col + dy
            if not self.within(board, new_row, new_col):
                continue
            self.search(board, new_row, new_col, node.char_child[curr_char], res)
            
        board[curr_row][curr_col] = curr_char
        
    def within(self, board, i, j):
        return 0<=i<len(board) and 0<=j<len(board[0])
