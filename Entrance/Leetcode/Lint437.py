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
            mid = (lower+upper)//2
            if self.can_copy(pages, k, mid):
                upper = mid
            else:
                lower = mid
                
        if self.can_copy(pages, k, lower):
            return lower
        return upper
            
    def can_copy(self, pages, k, timing): # easy made mistake
        need = 1
        currfinish = 0
        for page in pages:
            if currfinish + page > timing:
                need += 1
                currfinish = page
            else:
                currfinish += page
        return need <= k
