# 295. Find Median from Data Stream

'''
Solution 1:
Sort and get median
Time O(n^2logn)

Solution 2:
Insert sort and get median
Time O(n^2)

Solution 3:
Quick select and get median
Time O(n^2)

Solution 4:
Max heap + Min heap
Time O(nlogn)
'''

class Solution:
    """
    @param nums: A list of integers
    @return: the median of numbers
    """
    def medianII(self, nums):
        # write your code here
        import heapq
        minhp, maxhp = [], []
        res = []
        for num in nums:
            if len(minhp) == len(maxhp):
                heapq.heappush(minhp, num)
                heapq.heappush(maxhp, -heapq.heappop(minhp))
            else:
                heapq.heappush(maxhp, -num)
                heapq.heappush(minhp, -heapq.heappop(maxhp))
            res.append(-maxhp[0])
            
        return res
        