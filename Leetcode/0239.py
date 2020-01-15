# 239. Sliding Window Maximum

'''
Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

Example:

Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7] 
Explanation: 

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
'''


Solution 1: Brute force
use a deque to push and pop, get max by loop over the deque
Time O(nk)

Solution 2: Heapq with hashheap
use a heap to store current subarray, add new one and remove expired one,
removal needs O(n) time, but we can implement hashheap like in problem 480
Time O(nlogk)

Solution 3: Heapq without hashheap
Similar to the idea of 218.skyline,
we dont need to remove every num expired,
just remove the ones which expired but still on the top of the heap
Time O(nlogk)

class Solution:
    """
    @param nums: A list of integers.
    @param k: An integer
    @return: The maximum number inside the window at each moving.
    """
    def maxSlidingWindow(self, nums, k):
        # write your code here
        import heapq
        if not nums:
            return []
        
        hp = [(-num, i) for i, num in enumerate(nums[:k-1])]
        heapq.heapify(hp)
        left, right = 0, k-2
        
        res = []
        for i in range(k-1, len(nums)):
            heapq.heappush(hp, (-nums[i],i))
            
            while hp and hp[0][1] < left:
                heapq.heappop(hp)
            
            res.append(-hp[0][0])
            
            left += 1
            right += 1
        
        return res


Solution 4: Mono deque (recommend)
for num older and smaller, there's no reason to stay in the deque,
because it can never be the max,
so we can use deque to store a descending queue,
for each incoming num:
    if incoming num is greater, then pop all smaller out,
    while top num in the queue expired, also pop out

Time O(n)

class Solution:
    """
    @param nums: A list of integers.
    @param k: An integer
    @return: The maximum number inside the window at each moving.
    """
    def maxSlidingWindow(self, nums, k):
        # write your code here
        import collections
        if not nums:
            return []
        
        queue = collections.deque()
        for i, num in enumerate(nums[:k-1]): # save k-1 nums
            self.push(queue, num, i)
        
        left = 0
        res = []
        for i in range(k-1, len(nums)):
            num = nums[i]
            while queue and queue[0][1]<left: # expired num
                queue.popleft()
                
            self.push(queue, num, i) # push in new num

            res.append(queue[0][0])
            left += 1

        return res

    def push(self, queue, num, i):
        while queue and queue[-1][0]<=num:
            queue.pop()
        queue.append((num, i))
        