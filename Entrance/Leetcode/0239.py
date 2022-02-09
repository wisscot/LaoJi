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


Solution 2: Heapq w/ hashheap
use a heap to store current subarray, add new one and remove expired one,
removal needs O(n) time, but we can implement hashheap like in problem 480
Time O(nlogk)


Solution 2+: Heapq w/o hashheap
Similar to the idea of 218.skyline,
we dont need to remove every num expired,
just remove the ones which expired but still on the top of the heap
Time O(nlogk)


Solution 3: Mono deque (recommend)

for num older and smaller, there's no reason to stay in the deque,
because it can never be the max,
so we can use deque to store a descending queue,
for each incoming num:
    if incoming num is greater, then pop all smaller out from right,
    while top num in the queue expired, also pop it (popleft)

Time O(n)


# Solution 2+
class Solution:
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


# Solution 3
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = collections.deque()
        
        res = []
        for i, num in enumerate(nums):
            while queue and queue[-1][1] < num:
                queue.pop()
            queue.append((i, num))
            if queue[0][0] <= i - k:
                queue.popleft()
            
            if i >= k-1:
                res.append(queue[0][1])
                
        return res
        