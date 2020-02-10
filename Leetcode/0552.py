# 552. Student Attendance Record II

'''
Given a positive integer n, return the number of all possible attendance records with length n, which will be regarded as rewardable. The answer may be very large, return it after mod 109 + 7.

A student attendance record is a string that only contains the following three characters:

'A' : Absent.
'L' : Late.
'P' : Present.
A record is regarded as rewardable if it doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).
'''

Basic idea: DP


class Solution:
    def checkRecord(self, n: int) -> int:
        
        dp = [0] * (max(5, n+1))
        dp[0] = 1
        dp[1] = 2
        dp[2] = 4
        dp[3] = 7
        for i in range(4, n+1):
            dp[i] = (dp[i-1] * 2 - dp[i-4]) % 1000000007
        
        res = sum(dp[i]*dp[n-i-1] for i in range(n)) + dp[n]
        return res % 1000000007
            