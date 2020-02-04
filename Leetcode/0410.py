# 410. Split Array Largest Sum


'''
Given an array which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays. Write an algorithm to minimize the largest sum among these m subarrays.

Note:
If n is the length of array, assume the following constraints are satisfied:

1 ≤ n ≤ 1000
1 ≤ m ≤ min(50, n)
'''

Basic idea: Binary Search on result

Another way: DP (slower)

class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        lower, upper = max(nums), sum(nums)
        
        while lower < upper - 1:
            mid = (lower + upper) // 2
            if self.can_fit(nums, mid, m): # buckets num <= m
                upper = mid
            else:
                lower = mid
                
        if self.can_fit(nums, lower, m):
            return lower
        return upper
    
    def can_fit(self, nums, bucket_size, bucket_instock):
        bucket = 1
        accu = 0
        for num in nums:
            if accu + num > bucket_size:
                bucket += 1
                accu = num
            else:
                accu += num
        return bucket <= bucket_instock