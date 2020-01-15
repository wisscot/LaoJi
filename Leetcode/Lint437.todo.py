# 437. Copy Books

Basic idea:
guess and answer, verify it using greedy approach
prove of the greedy:
    if in a correct solution, a person has less book 
    then we can get book from others
    and the answer would still be valid


class Solution:
    """
    @param pages: an array of integers
    @param k: An integer
    @return: an integer
    """
    def copyBooks(self, pages, k):
        # write your code here
        if not pages:
            return 0
            
        lower, upper = max(pages), sum(pages)
        
        while lower < upper - 1:
            mid = (lower+upper) // 2
            if self.numperson(pages, mid) <= k: 
            # when equals, move upper, because result can be smaller
                upper = mid
            else:
                lower = mid
                
        if self.numperson(pages, lower) <= k:
            return lower
        return upper
        
    def numperson(self, pages, timeperiod):
        res = 1
        
        cumu = 0
        for page in pages:
            if cumu + page > timeperiod:
                cumu = page
                res += 1
            else:
                cumu += page
                
        return res
