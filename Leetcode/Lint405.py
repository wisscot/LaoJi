# 405. Submatrix Sum

'''
Given an integer matrix, find a submatrix where the sum of numbers is zero. Your code should return the coordinate of the left-up and right-down number.

If there are multiple answers, you can return any of them.
'''

Basic idea: Prefix sum

Solution 1:
calculation matrix prefix sum
then enumerate left top corners and right bottom corners 
Time: O(n^4)

Solution 2:
fix row i,j
treat col[i...j] as one num
then we can apply subarray prifix sum
Time: O(n^3)

# Solution 2
class Solution:
    """
    @param: matrix: an integer matrix
    @return: the coordinate of the left-up and right-down number
    """
    def submatrixSum(self, matrix):
        # write your code here
        res = []
        for i in range(len(matrix)):
            prefixsum = [0] 
            for num in matrix[i]:
                prefixsum.append(prefixsum[-1]+num)
            
            for i_ in range(i, len(matrix)):
                if i_>i:
                    prefixsum_ = [0]
                    for num in matrix[i_]:
                        prefixsum_.append(prefixsum_[-1]+num)
                    for j in range(len(prefixsum)):
                        prefixsum[j] += prefixsum_[j]
                        
                sum_index = {}
                for j, num in enumerate(prefixsum):
                    if num in sum_index:
                        return [[i, sum_index[num]], [i_, j-1]]
                    sum_index[num] = j
                    
                    
                        
                
