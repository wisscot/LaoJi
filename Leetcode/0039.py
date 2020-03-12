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

                            remaining=target
                2/             3 /        7/   \..   \..
            target-2        target-3     ...     ....
        2/ 3/ /7 \..       3/ 7/ \..           
target-2-2

if remain == 0: save and return  
if remain < 0: just return           

# Solution
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.search(candidates, 0, target, [], res)
        return res
    
    def search(self, nums, start_idx, remain, path, res):
        if remain < 0:
            return
        
        if remain == 0:
            res.append(list(path))
            return
        
        for i in range(start_idx, len(nums)):
            path.append(nums[i])
            self.search(nums, i, remain-nums[i], path, res)
            path.pop()
            
        
