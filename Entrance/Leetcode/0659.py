# 659. Split Array into Consecutive Subsequences

'''
Given an array nums sorted in ascending order, return true if and only if you can split it into 1 
or more subsequences such that each subsequence consists of consecutive integers and has length at 
least 3.
'''

Basic idea: Greedy

Note the array is in non-decrease order. 

arrays = [
    [1,2,3,4],
    [2,3,4,5,6],
    [1,2,3],
    ...
]
nums = [1,1,2,2,2,3,3,3,4,4,5,6,7,7,8, ... ]
                                ^
                            current num

Sweep num in nums, save them to a nested list arrays
For a num in nums, there are two options:
    1. append it to existing array
    2. start a new array with [num, num+1, num+2]

Which one should have higher priority? First one
There are two cases: 
one, this num can not find three consecutive nums,
    in this case, we have to append it to existing array
two, we can find three consecutive nums,
    in this case, if we append these three nums to an array,
    it does not affect the result
so, append to existing array is preferred.


Solution 1. O(n^2)
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        arrays = []
        while nums:
            num = nums.pop(0)
            if self.can_append(arrays, num-1):
                self.array_append(arrays, num)
            elif self.has_three_consecutive(nums, num):
                self.arrays_add(arrays, num)
                self.nums_remove_followtwo(nums, num)
            else:
                return False
        return True
                    
    def can_append(self, arrays, num):
        for arr in arrays:
            if num == arr[-1]:
                return True
        return False
    
    def array_append(self, arrays, num):
        for arr in arrays:
            if num-1 == arr[-1]:
                arr.append(num)
                return
    
    def has_three_consecutive(self, nums, num):
        return num+1 in nums and num+2 in nums
    
    def arrays_add(self, arrays, num):
        arrays.append([num, num+1, num+2])
        
    def nums_remove_followtwo(self, nums, num):
        nums.remove(num+1)
        nums.remove(num+2)
        
        
Solution 2: Improved with count  O(n)
Actually only the last num of each array matters,
so no need to keep the array but only the last number of array

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        remain_count = collections.Counter(nums)
        tail_count = collections.Counter()
        
        for num in nums:
            if remain_count[num] == 0:
                continue
            remain_count[num] -= 1
            if tail_count[num-1]>0:
                tail_count[num-1] -= 1
                tail_count[num] += 1
            elif remain_count[num+1]>0 and remain_count[num+2]>0:
                remain_count[num+1] -= 1
                remain_count[num+2] -= 1
                tail_count[num+2] += 1
            else:
                return False
            
        return True