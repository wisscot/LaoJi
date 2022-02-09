# 215. Kth Largest Element in an Array

'''
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.
'''

Solution 1: Sort
Time: O(nlogn)


Solution 2: Quick Select
Easy to understand, use extra space
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        pivot = random.choice(nums)
        
        lt = [num for num in nums if num < pivot]
        eq = [num for num in nums if num == pivot]        
        gt = [num for num in nums if num > pivot]
        
        if k <= len(gt):
            return self.findKthLargest(gt, k)
        elif k > len(eq) + len(gt):
            return self.findKthLargest(lt, k-len(gt) - len(eq))
        else:
            return pivot
            
        
Solution 3: QuickSelect Classic
Similar to QuickSort
def quick_select(self, nums, k, left, right):
    pivot = nums[right]
    # ...ssssssbbbbbbsbsbsbp...
    #    l     j     i     r
    j = left
    for i in range(left, right):
        if nums[i] > pivot:
            self.swap(nums, i, j)
            j += 1
    self.swap(nums, j, right)
    # ...sssssspbbbbbbbbbbbb...
    #    l     j          ir
    if k <= j-left:
        return self.find(nums, k, left, j-1)
    if k > j+1-left:
        return self.find(nums, k-(j+1-left), j+1, right)
    return pivot
    
    
Solution 4: Heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        nums = [-num for num in nums]
        heapq.heapify(nums)
        
        for _ in range(k):
            res = -heapq.heappop(nums)
            
        return res