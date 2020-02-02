# 15. 3Sum

'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''

Basic idea: reduce to Two Sum
be caution with duplicates

Solution 1: Sort and solve with two pointers
Sorting if good for duplicates removal

Solution 2: Alternative: with hashmap  (not recommended)
need to check if two equal element sum == target, and if three 0 existes
too many special cases, easy to make mistake 

# Solution 1
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        
        res = []
        for i in range(len(nums)-2):
            if i and nums[i] == nums[i-1]:
                continue
            self.twosum(nums, i+1, len(nums)-1, -nums[i], res)
                
        return res
    
    def twosum(self, nums, left, right, target, res):
        right = len(nums) - 1
        i, j = left, right
        while i < j:
            if nums[i] + nums[j] < target:
                i += 1
            elif nums[i] + nums[j] > target:
                j -= 1
            else:
                res.append([-target, nums[i],nums[j]])
                i += 1
                j -= 1
                
                # skip duplicates
                # Caution: only move while one pair found!
                while i and i<j and nums[i] == nums[i-1]:
                    i += 1
                while j<right and i<j and nums[j] == nums[j+1]:
                    j -= 1
                        
                
                
# Solution 2 (not recommend)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        count = collections.Counter(nums)
        uniques = sorted(count.keys())
        
        res = []
        for i, num in enumerate(uniques):
            self.twosum(uniques, i+1, len(uniques)-1, -num, res)
            if num % 2 == 0 and count[-num//2] >= 2 and num != 0:
                res.append([num, -num//2, -num//2])
                
        if count[0] >= 3:
            res.append([0, 0, 0])
            
        return res
    
    def twosum(self, nums, left, right, target, res):
        visited = set()
        for num in nums[left:right+1]:
            if target-num in visited:
                res.append([-target, num, target-num])
            visited.add(num)
                                    
                