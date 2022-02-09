480. Sliding Window Median

Solution 1: Brute Force
basic idea is to maintain a sorted list with length k
add a incoming number and remove a outgoing number
Time O(nk)

Solution 2: Heap - Hash Heap
basic idea is using min and max heap, just like "median of data stream"
however, heapq does not support remove in logn time,
so we have to implement it, called hashheap
Time O(nlogk)

Solution 3: Heap - Lazy Heap
basic idea is using min and max heap, just like "median of data stream"
Just like in 218.skyline problem, we dont have to delete at the moment its out of the window
Just delete when it comes to the top of the queue
Time O(nlogk)


# Solution 1
class Solution:
    """
    @param nums: A list of integers
    @param k: An integer
    @return: The median of the element inside the window at each moving
    """
    def medianSlidingWindow(self, nums, k):
        # write your code here
        if not nums:
            return []
        array = nums[:k-1]
        res = []
        
        array.sort()
        for i in range(k-1, len(nums)):
            bisect.insort(array, nums[i])
            res.append(array[(k-1)//2])
            index = bisect.bisect_left(array, nums[i-k+1])
            array.pop(index)
            
        return res

# Solution 3
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        
        if k == 1: # special case 
            return nums
        
        minhqueue = nums[:k]
        heapq.heapify(minhqueue)
        maxhqueue = []
        for _ in range(k//2):
            heapq.heappush(maxhqueue, -heapq.heappop(minhqueue))
            
        expired = collections.Counter()
        
        res = [self.get_median(minhqueue, maxhqueue, k)]

        for i in range(k, len(nums)):
            
            # add
            if nums[i-k] >= minhqueue[0]:
                heapq.heappush(maxhqueue, -nums[i])
                heapq.heappush(minhqueue, -heapq.heappop(maxhqueue))
            else:
                heapq.heappush(minhqueue, nums[i])
                heapq.heappush(maxhqueue, -heapq.heappop(minhqueue))
            
            # delete
            if i > k - 1:
                expired[nums[i-k]] += 1
            self.remove_expired_top(minhqueue, maxhqueue, expired)

            # save result
            res.append(self.get_median(minhqueue, maxhqueue, k))
        
        return res
        
    def get_median(self, minhqueue, maxhqueue, k):
        if k & 1:
            return minhqueue[0]
        else:
            return (minhqueue[0]-maxhqueue[0])/2
        
    def remove_expired_top(self, minhqueue, maxhqueue, expired):
        while expired[minhqueue[0]]:
            expired[minhqueue[0]] -= 1 # do this first before pop
            heapq.heappop(minhqueue)
        while expired[-maxhqueue[0]]:
            expired[-maxhqueue[0]] -= 1
            heapq.heappop(maxhqueue)
        