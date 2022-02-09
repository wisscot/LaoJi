# 1326. Minimum Number of Taps to Open to Water a Garden

'''
There is a one-dimensional garden on the x-axis. The garden starts at the point 0 and ends at the point n. (i.e The length of the garden is n).

There are n + 1 taps located at points [0, 1, ..., n] in the garden.

Given an integer n and an integer array ranges of length n + 1 where ranges[i] (0-indexed) means the i-th tap can water the area [i - ranges[i], i + ranges[i]] if it was open.

Return the minimum number of taps that should be open to water the whole garden, If the garden cannot be watered return -1.
'''

Basic idea: Sweep Line
Greedy approach, save furthest location a start point can jump to
sweep all the positions 

Solution 1:
class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        jump = [0]*(n+1)
        key_pos = []
        for i, cover in enumerate(ranges):
            if cover:
                start, end = max(0,i-cover), min(n,i+cover)
                jump[start] = max(jump[start], end) 
                key_pos += [start, end]
                
        key_pos = sorted(set(key_pos))

        res = 0
        curr_end = next_end = 0
        for pos in key_pos:
            next_end = max(jump[pos], next_end)
            if pos == curr_end:            
                curr_end = next_end
                res += 1
                if curr_end == n:
                    return res
        return -1
            
            
Solution 2: same idea, not sweeping, but jump
class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        jump = [0]*(n+1)
        for i, cover in enumerate(ranges):
            if cover:
                start, end = max(0,i-cover), min(n,i+cover)
                jump[start] = max(jump[start], end)

        res = 0
        curr = prev = 0
        while curr < n:
            res += 1
            prev, curr = curr, max(jump[prev:curr+1]) # jump prev and curr at the SAME time 
            if curr == prev: # if not moving
                return -1
        return res
            
            