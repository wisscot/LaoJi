# 611. Valid Triangle Number

'''
Basic idea:
convert to two sum by sorting and use longest side as master pointer

Time: O(n^2)
'''


class Solution:
    """
    @param S: A list of integers
    @return: An integer
    """
    def triangleCount(self, S):
        # write your code here
        S.sort()
        res = 0
        for i in range(len(S)):
            left, right = 0, i-1
            while left < right:
                if S[right] + S[left] > S[i]:
                    res += right - left
                    right -= 1
                else:
                    left += 1
                
        return res
