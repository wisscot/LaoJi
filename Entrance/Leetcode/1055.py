# 1055. Shortest Way to Form String

'''
From any string, we can form a subsequence of that string by deleting some number of characters (possibly no deletions).

Given two strings source and target, return the minimum number of subsequences of source such that their concatenation equals target. If the task is impossible, return -1.
'''

Basic idea:
greedy

Time O(n^2)

Follow ups:
1. Time O(nlogn)
2. Time O(n)


class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        res = 1
        
        idx = -1 # for source
        for t in target:
            next_idx = source.find(t, idx+1)
            if next_idx > -1:
                idx = next_idx
                continue
                
            next_idx = source.find(t)
            if next_idx == -1:
                return -1
            res += 1
            idx = next_idx
            
        return res
            
                