# 405. Submatrix Sum

'''
Given an integer matrix, find a submatrix where the sum of numbers is zero. Your code should return the coordinate of the left-up and right-down number.

If there are multiple answers, you can return any of them.
'''

Basic idea: Prefix sum

Solution 1:
calculation matrix prefix sum
then enumerate left top corners and right bottom corners 
Time: O((mn)^2)

Solution 2:
fix row i,j
treat col[i...j] as one tall cell
then we can reduce it to subarray prefixsum
Time: O(m*m*n)

# Solution 2
class Solution:
    """
    @param: matrix: an integer matrix
    @return: the coordinate of the left-up and right-down number
    """
    def submatrixSum(self, matrix):
        # write your code here
        m, n = len(matrix), len(matrix[0])
        for i in range(len(matrix)):
            tall_cells = [0] * n
            for j in range(i, m):
                for k in range(n):
                    tall_cells[k] += matrix[j][k]
                res = self.subarraySum(tall_cells)
                if res:
                    col_1, col_2 = res
                    return [[i, col_1], [j, col_2]]

    def subarraySum(self, nums):
        n = len(nums)
        presum = [0]
        for num in nums:
            presum.append(presum[-1]+num)

        sum_index = {}
        for i, psum in enumerate(presum):
            if psum in sum_index:
                return sum_index[psum], i-1
            sum_index[psum] = i
                    
                        
                

                    
                        
                
