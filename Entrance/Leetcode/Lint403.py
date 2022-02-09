# 403. Continuous Subarray Sum II

'''
Given an circular integer array (the next element of the last element is the first element), find a continuous subarray in it, where the sum of numbers is the biggest. Your code should return the index of the first number and the index of the last number.

If duplicate answers exist, return any of them.
'''

Basic idea: Prefix Sum

Array -> Circle 
Separate the problem into two parts:
1. result not across end-start connection, this case is same as no circle
2. result across the circle connections, in this case, the remaining sum is the minimum


class Solution:
    """
    @param: A: An integer array
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def continuousSubarraySumII(self, A):
        # write your code here
        psums = [0]
        for a in A:
            psums.append(psums[-1]+a)
        # psums[j] = sum A[0] .. A[j-1]
        
        maxsubsum1, res1 = self.findmax(psums)
        minsubsum2, res2 = self.findmax([-x for x in psums])
        minsubsum2 *= (-1)

        if maxsubsum1 >= psums[-1] - minsubsum2:
            return res1
        if res2[0] == 0 or res2[1] == len(A)-1:
            return res1
        return[res2[1]+1, res2[0]-1]
        
    def findmax(self, psums):
        
        minindex = 0
        maxindex = 0
        maxdiff = float('-inf')
        for i in range(1, len(psums)):
            if psums[i]-psums[minindex] > maxdiff:
                maxdiff = psums[i]-psums[minindex]
                maxindex = i-1
                res = [minindex, maxindex]
            
            if psums[i] < psums[minindex]:
                minindex = i
                
        return maxdiff, res
        
        
        
        