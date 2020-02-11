# 264. Ugly Number II

'''
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 
'''

Basic idea: Heapq
Get the minimum number of current calculated and multiply 2, 3 and 5


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        nums = [1]
        visited = set([1])
        
        for i in range(n):
            current = heapq.heappop(nums)
            for mult in [2,3,5]:
                child = current*mult
                if child in visited:
                    continue
                heapq.heappush(nums, child)
                visited.add(child)
                
        return current