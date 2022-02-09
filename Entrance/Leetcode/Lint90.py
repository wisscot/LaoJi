# 90. k Sum II

'''
Given n unique postive integers, number k (1<=k<=n) and target.
Find all possible k integers where their sum is target.
'''

Basic idea: DFS


class Solution:
    def kSumII(self, A, k, target):
        # write your code here
        
        A.sort()
        
        res = []
        self.search(A, 0, k, target, [], res)
        return res
        
    def search(self, A, start, k, target, path, res):
        if target < 0:
            return
        
        if k == 0:
            if target == 0:
                res.append(list(path))
            else:
                return
        
        for i in range(start, len(A)):
            path.append(A[i])
            self.search(A, i+1, k-1, target-A[i], path, res)
            path.pop()
        