# 1231. Divide Chocolate

'''
You have one chocolate bar that consists of some chunks. Each chunk has its own sweetness given by the array sweetness.

You want to share the chocolate with your K friends so you start cutting the chocolate bar into K+1 pieces using K cuts, each piece consists of some consecutive chunks.

Being generous, you will eat the piece with the minimum total sweetness and give the other pieces to your friends.

Find the maximum total sweetness of the piece you can get by cutting the chocolate bar optimally.
'''

Very similar to 410, which is minimize the max, this one is to maximize the minimum


Soluiton 1. Binary Seach
Be careful of the check function, not same as 410

Solution 2. DP (slower)


# Solution 1
class Solution:
    def maximizeSweetness(self, sweetness: List[int], K: int) -> int:
        
        lower, upper = min(sweetness), sum(sweetness)
        while lower < upper - 1:
            mid = (lower + upper) // 2
            if self.can_cut(sweetness, K+1, mid):
                lower = mid
            else:
                upper = mid
                
        if self.can_cut(sweetness, K+1, upper):
            return upper
        return lower
    
    def can_cut(self, sweets, person, target):
        accu = 0
        box = 0
        
        for sweet in sweets:
            accu += sweet
            if accu >= target:
                box += 1
                accu = 0

        return box >= person
 