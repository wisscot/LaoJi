# 402. Continuous Subarray Sum

'''
Given an integer array, find a continuous subarray where the sum of numbers is the biggest. Your code should return the index of the first number and the index of the last number. (If their are duplicate answer, return the minimum one in lexicographical order)
'''

Basic idea: prefix sum
global max gap = max of all {curr - min happened before}

class Solution:
    """
    @param: A: An integer array
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def continuousSubarraySum(self, A):
        # write your code here
        
        psums = [0]
        for a in A:
            psums.append(psums[-1]+a)
            
        # psum[i] = sum A[0] ... A[i-1]
        
        prevmin = [float('inf'), -1]
        maxsum = float('-inf')
        res = []
        
        for i, psum in enumerate(psums):
            if i>0 and maxsum < psum - prevmin[0]:
                maxsum = psum - prevmin[0]
                res = [prevmin[1], i-1]
            if psum < prevmin[0]:
                prevmin = [psum, i]
                
        return res


