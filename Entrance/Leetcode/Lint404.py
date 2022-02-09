# 404. Subarray Sum II

'''
Given an positive integer array A and an interval. Return the number of subarrays whose sum is in the range of given interval.
'''

Basic idea: Prefix sum + two pointers

we can use two pointers because all nums are positive so the presum are increasing

class Solution:
    """
    @param A: An integer array
    @param start: An integer
    @param end: An integer
    @return: the number of possible answer
    """
    def subarraySumII(self, A, start, end):
        # write your code here
        
        psum = [0]
        for a in A:
            psum.append(psum[-1]+a)
        # psum[i] is sum A[0] ... A[i-1]
        
        # x x x v v v x x x 
        #       ^     ^     ^
        #       l     r     i
        l = r = res = 0
        for i in range(1, len(psum)):
            
            while psum[i] - psum[l] > end and l < i:
                l += 1
                
            while psum[i] - psum[r] >= start and r < i:
                r += 1
                
            res += r - l
            
        return res
