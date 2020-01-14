480. Sliding Window Median

Solution 1:
basic idea is to maintain a sorted list with length k
add a incoming number and remove a outgoing number
Time O(nk)

Solution 2:
basic idea is using min and max heap, just like "median of data stream"
however, heapq does not support remove in logn time,
so we have to implement it, called hashheap
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
        import bisect
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

# Solution 2
todo