# 287. Find the Duplicate Number

'''
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), 
prove that at least one duplicate number must exist. Assume that there is only one duplicate number, 
find the duplicate one.

Example 1:
Input: [1,3,4,2,2]
Output: 2

Example 2:
Input: [3,1,3,4,2]
Output: 3
'''

Solution 1: (recommend)
Basic idea is there must exist a duplicate num x, 
if we count the number based on value, 
then for any num between 1 to x-1, the count will be <= num
for num x and above, the count will be > num
the array   1, 2, ...., x-1, x, x, x, x, x+1, x+2, ...
                    ^              ^                ^
count (<=num)    count<=num      count>num        count>num

so we can use binary search

Time O(nlogn)

class Solution:
    """
    @param nums: an array containing n + 1 integers which is between 1 and n
    @return: the duplicate one
    """
    def findDuplicate(self, nums):
        # write your code here
        lower, upper = min(nums), max(nums)
        
        while lower < upper - 1:
            mid = (lower+upper)//2
            if self.countle(nums, mid) <= mid:
                lower = mid
            else:
                upper = mid
                
        if self.countle(nums, lower) > lower:
            return lower
        return upper
        
    def countle(self, nums, target):
        ct = 0
        for num in nums:
            if num <= target:
                ct += 1
                
        return ct



Solution 2: (difficult to come up with in interview)
use value as index so it becomes a linked list with cycle, the entry point is the duplicate number
''' from leetcode discussion
If there is no duplicate in the array, we can map each indexes to each numbers in this array. In other words, we can have a mapping function f(index) = number
For example, let's assume
nums = [2,1,3], then the mapping function is 0->2, 1->1, 2->3.
If we start from index = 0, we can get a value according to this mapping function, and then we use this value as a new index and, again, we can get the other new value according to this new index. We repeat this process until the index exceeds the array. Actually, by doing so, we can get a sequence. Using the above example again, the sequence we get is 0->2->3. (Because index=3 exceeds the array's size, the sequence terminates!)
However, if there is duplicate in the array, the mapping function is many-to-one.
For example, let's assume
nums = [2,1,3,1], then the mapping function is 0->2, {1,3}->1, 2->3. Then the sequence we get definitely has a cycle. 0->2->3->1->1->1->1->1->........ The starting point of this cycle is the duplicate number.
'''

