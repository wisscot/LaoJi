# 586. Sqrt(x) II

Basic idea:
result based binary search on decimals

class Solution:
    """
    @param x: a double
    @return: the square root of x
    """
    def sqrt(self, x):
        # write your code here
        low, high = 0, x+1 # this is to consider cases of 0<x<1
            
        while low < hight - 1e-10:
            mid = (low+high)/2
            if mid*mid < x:
                low = mid
            else:
                high = mid
                
        return mid