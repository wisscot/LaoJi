# 1007. Minimum Domino Rotations For Equal Row

'''
In a row of dominoes, A[i] and B[i] represent the top and bottom halves of the i-th domino.  (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the i-th domino, so that A[i] and B[i] swap values.

Return the minimum number of rotations so that all the values in A are the same, or all the values in B are the same.

If it cannot be done, return -1.
'''


Basic idea: (from leetcode discussion)
One observation is that, if A[0] works, no need to check B[0].
Because if both A[0] and B[0] exist in all dominoes,
when you swap A[0] in a whole row,
you will swap B[0] in a whole at the same time.
The result of trying A[0] and B[0] will be the same.


class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        if all(A[0] in pair for pair in zip(A,B)): # see if A[0] in all card
            return len(A) - max(A.count(A[0]), B.count(A[0])) # remove duplicates
        if all(B[0] in pair for pair in zip(A,B)):
            return len(B) - max(A.count(B[0]), B.count(B[0]))
        return -1


