# 39. Combination Sum

'''
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
'''

Basic idea: DFS
make the nums unique and sorted
when do next level search, keep start unchanged because a num can be used mutiple times

class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """
    def combinationSum(self, candidates, target):
        # write your code here
        if not candidates:
            return []
            
        nums = sorted(list(set(candidates)))
        res = []
        self.search(nums, 0, target, [], res)
        
        return res
        
    def search(self, nums, start, target, path, res):
        
        if target < 0:
            return 
        
        if target == 0:
            res.append(list(path))
            
        for i in range(start, len(nums)):
            path.append(nums[i])
            self.search(nums, i, target-nums[i], path, res)
            path.pop()
            
        
