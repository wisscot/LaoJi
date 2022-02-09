# 46. Permutations

'''
Given a collection of distinct integers, return all possible permutations.
Example:
Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''

Basic idea: DFS

Solution 1: Regular backtracking
                            visited=()
                2/             3 /        7/   \..   \..
            visited=(2)       (3)       (7)     ....
        2/ 3/       /7 \..  2/ 3/ 7/ \..           
       X  (2,3) 
          / / \7\.. 
         X X  (2,3,7)


# Solution 1
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        visited = set()
        self.search(nums, visited, [], res)
        return res
    
    def search(self, nums, visited, path, res):
        if len(visited) == len(nums):
            res.append(list(path))
            
        for i, num in enumerate(nums):
            if i in visited:
                continue
            path.append(num)
            visited.add(i)
            self.search(nums, visited, path, res)
            visited.remove(i)
            path.pop()

            
        
        