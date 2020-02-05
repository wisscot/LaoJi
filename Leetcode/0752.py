# 752. Open the Lock

'''
You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.

The lock initially starts at '0000', a string representing the state of the 4 wheels.

You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.

Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.
'''


Basic idea: BFS


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        deadends = set(deadends)
        
        queue = collections.deque(['0000'])
        visited = set(['0000'])
        
        level = -1
        while queue:
            level += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                if node in deadends:
                    continue
                if node == target:
                    return level
                
                for neib in self.neibs(node):
                    if neib in visited:
                        continue
                    queue.append(neib)
                    visited.add(neib)
        
        return -1
    
    def neibs(self, s):
        res = []
        for i, ch in enumerate(s):
            num = int(ch)
            res.append(s[:i] + str((num - 1) % 10) + s[i+1:])
            res.append(s[:i] + str((num + 1) % 10) + s[i+1:])
        return res
    