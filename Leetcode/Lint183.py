# 183. Wood Cut

Basic idea:
if we guess an answer, we can verify it correct or not,
so we can try all the result -> Binary search on result


class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    @return: The maximum length of the small pieces
    """
    def woodCut(self, L, k):
        # write your code here
        lower, upper = 1, max(L or [0])
        
        while lower < upper - 1:
            mid = (lower+upper)//2
            if self.count(L, mid) < k:
                upper = mid
            else:
                lower = mid
                
        if self.count(L, upper) >= k:
            return upper
        if self.count(L, lower) >= k:
            return lower
        return 0

    def count(self, L, num):
        return sum([leng//num for leng in L])