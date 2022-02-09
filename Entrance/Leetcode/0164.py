# 164. Maximum Gap

'''
Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

Return 0 if the array contains less than 2 elements.
'''

Basic idea:
Sort integer array in O(n) time


Solution 1 - Radix Sort
Sort integer array using radix sort by sorting digit from front to end
with couting sort


Solution 2 - Bucket Sort
the average gap is (max-min)/(n-1)
so the max gap is at least (max-min)/(n-1)
so if we use bucket with size <= max gap,
we only need to maintain the bucket's max and min

we set size = (max-min) // (n-1) or 1
num of buckets = (max-min)//size + 1

num will be put into bucket #
(num-min) // size

finally, get all nums from bucket and calculate max gap

# Solution 1. Radix Sort
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        
        if len(nums) < 2:
            return 0
        
        nums = self.radixsort(nums)
        
        res = 0
        for i in range(len(nums)-1):
            res = max(res, nums[i+1]-nums[i])
            
        return res
            
    def radixsort(self, nums):
        
        d = len(str(max(nums)))
        
        for i in range(d):
            nums = self.coutingsort(nums, i)
            
        return nums
    
    def coutingsort(self, nums, i):
        # i = 0, 1, ... ,d
        # bar = 1, 10, 100, ...
        
        buckets = [[] for _ in range(10)]
        bar = 10**i 
        
        for num in nums:
            idx = num//bar%10  # get reverse ith digit
            buckets[idx].append(num)  

        res = []
        for bucket in buckets:
            res += bucket
            
        return res
            
        
# Solution 2: Buckets Sort
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        
        if len(nums) < 2: 
            return 0
        
        maxnum, minnum = max(nums), min(nums)
        size = (maxnum-minnum) // (len(nums)-1) or 1
        
        buckets = [[float('inf'), float('-inf')] for _ in range((maxnum-minnum)//size + 1)]
        
        for num in nums:
            idx = (num-minnum) // size
            buckets[idx][0] = min(num, buckets[idx][0])
            buckets[idx][1] = max(num, buckets[idx][1])
            
        arr = [num for b in buckets for num in b if float('-inf')<b[0]<float('inf')]
        return max(arr[i] - arr[i-1] for i in range(1, len(arr)))