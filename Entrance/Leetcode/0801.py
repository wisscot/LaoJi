# 801. Minimum Swaps To Make Sequences Increasing

'''
We have two integer sequences A and B of the same non-zero length.

We are allowed to swap elements A[i] and B[i].  Note that both elements are in the same index position in their respective sequences.

At the end of some number of swaps, A and B are both strictly increasing.  (A sequence is strictly increasing if and only if A[0] < A[1] < A[2] < ... < A[A.length - 1].)

Given A and B, return the minimum number of swaps to make both sequences strictly increasing.  It is guaranteed that the given input always makes it possible.
'''

Basic idea: DP
save two states

class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        INF = float('inf')
        n = len(A)
        noswap = [0] + [INF] * (n-1)
        swap = [1] + [INF] * (n-1)
        
        for i in range(1, n):
            if A[i] > A[i-1] and B[i] > B[i-1]:
                swap[i] = min(swap[i], 1+swap[i-1])
                noswap[i] = min(noswap[i], noswap[i-1])
            if A[i] > B[i-1] and B[i] > A[i-1]:
                swap[i] = min(swap[i], 1+noswap[i-1])
                noswap[i] = min(noswap[i], swap[i-1])
                
        return min(swap[-1], noswap[-1])
