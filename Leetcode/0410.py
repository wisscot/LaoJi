# 410. Split Array Largest Sum


'''
Given an array which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays. Write an algorithm to minimize the largest sum among these m subarrays.

Note:
If n is the length of array, assume the following constraints are satisfied:

1 ≤ n ≤ 1000
1 ≤ m ≤ min(50, n)
'''

Solution 1: Binary Search on result

Solution 2: DP (slower)


# Solution 1. Binary Search
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
        
        
# Solution 2. DP
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        if not nums: return 0
        accums = [0]
        for num in nums:
            accums.append(accums[-1]+num)
            
        n = len(nums)
        T = [[0]*(n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if i > j:
                    continue
                if i == 1:
                    T[i][j] = accums[j]
                    continue
                T[i][j] = min([max(T[i-1][j-1-k], accums[j]-accums[j-k-1]) for k in range(j-i+1)])
        return T[-1][-1]
    