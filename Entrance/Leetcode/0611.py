# 611. Valid Triangle Number

'''
Given an array consists of non-negative integers, your task is to count the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.
Example 1:
Input: [2,2,3,4]
Output: 3
Explanation:
Valid combinations are: 
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3
'''


Basic idea:
convert to two sum by sorting and use longest side as master pointer

in sorted array
1, 2, 3, 4, 5, 6, 7, 8, ...
^                    ^
i                    j
if sum [i], [j] > target, then all num between i to j + [j]  > target
so res += j - i
midset: keep an eye on j

Time: O(n^2)


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
