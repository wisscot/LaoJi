# Lint143. Sort Colors II

'''
Given an array of n objects with k different colors (numbered from 1 to k), sort them so that objects of the same color are adjacent, with the colors in the order 1, 2, ... k.
'''

Solution 1: Counting Sort (Naive)
Time O(n)    Space O(k)

Solution 2: Quick Sort idea (preferred)
Time O(nlogk)    Space O(1)

Solution 2+: Quick Sort idea, three parts each time (use [75. Sort Colors])
Time O(nlogk)    Space O(1)

# Solution 2
class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sortColors2(self, colors, k):
        # write your code here
        self.sort(colors, 1, k, 0, len(colors)-1)
        
    def sort(self, colors, lower, upper, left, right):
        
        if lower == upper:
            return
        
        mid = (lower+upper)//2
        # ....ssssssgggggsgs....gsgss...
        #     l     i    j          r
        i = left  # ! made mistake mutiple times to assign j=0 !
        for j in range(left, right+1):
            if colors[j] <= mid:
                colors[i], colors[j] = colors[j], colors[i]
                i += 1
        # ....seseseggggggggggggggggg
        #     l     i               r
        self.sort(colors, lower, mid, left, i-1)
        self.sort(colors, mid+1, upper, i, right)
        
        
        
# Solution 2+: lt, eq, gt  3 parts version
class Solution:
    def sortColors2(self, colors, k):
        self.sort(colors, 1, k, 0, len(colors)-1)
        
    def sort(self, colors, lower, upper, left, right):
        
        if lower >= upper:
            return
        
        pivot = (lower + upper) // 2
        # ....sssssseeeeesge....ggggg
        #     l     j    i     k    r
        i, j, k = left, left, right
        while i <= k:  # check right bound is k not right
            if colors[i] == pivot:
                i += 1
            elif colors[i] < pivot:
                self.swap(colors, i, j)
                j += 1
                i += 1
            else:
                self.swap(colors, i, k)
                k -= 1

        # ....sssssseeeeeeeeggggggggg
        #     l     j      k        r
        self.sort(colors, lower, pivot-1, left, j-1)
        self.sort(colors, pivot+1, upper, k+1, right)
        
    def swap(self, arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]