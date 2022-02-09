# 1048. Longest String Chain

'''
Given a list of words, each word consists of English lowercase letters.

Let's say word1 is a predecessor of word2 if and only if we can add exactly one letter anywhere in word1 to make it equal to word2.  For example, "abc" is a predecessor of "abac".

A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >= 1, where word_1 is a predecessor of word_2, word_2 is a predecessor of word_3, and so on.

Return the longest possible length of a word chain with words chosen from the given list of words.
'''

Basic idea:
build a graph and find the length of the longest tree

Solution 1: DFS

Solution 2: Topological sort

Solution 3: DP

# Solutoin 3
def longestStrChain(self, words: List[str]) -> int:
    
    words.sort(key=len)
    dp = {}
    for word in words:
        dp[word] = max(1 + dp.get(word[:i]+word[i+1:], 0) for i in range(len(word)))
                    
    return max(dp.values())
    
        