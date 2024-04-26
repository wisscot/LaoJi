# 78. Subsets

'''
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.
'''

Basic idea: DFS

# take it or not take it, e.g.  'abc'
#                                 ''
#                take 'a'/                \ not take 'a'     
#                  'a'                    ''
#         take 'b'/   \not take 'b'      /   \
#               'ab'   'a'            ...     ...
#     take 'c'/   \.. ../\..   
#         'abc'   'ab'    

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.search(nums, 0, [], res)
        return res
    
    def search(self, nums, index, path, res):
        if index == len(nums):
            res.append(list(path))
            return
            
        # not take
        self.search(nums, index+1, path, res)
        
        # take
        path.append(nums[index])
        self.search(nums, index+1, path, res)
        path.pop()