# 821. Time Intersection

Basic idea:
think it as plane take off and touch down, then -> the Lintcode391 planes in the sky problem

use dictionary to store all the information at each key event, like in the skyline problem



'''Description
Give two users' ordered online time series, and each section records the user's login time point x and offline time point y. Find out the time periods when both users are online at the same time, and output in ascending order.you need return a list of intervals.

We guarantee that the length of online time series meet 1 <= len <= 1e6.
For a user's online time series, any two of its sections do not intersect.

Example 1:

Input: seqA = [(1,2),(5,100)], seqB = [(1,6)]
Output: [(1,2),(5,6)]
Explanation: In these two time periods (1,2), (5,6), both users are online at the same time.
Example 2:

Input: seqA = [(1,2),(10,15)], seqB = [(3,5),(7,9)]
Output: []
Explanation: There is no time period, both users are online at the same time.
'''


"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param seqA: the list of intervals
    @param seqB: the list of intervals
    @return: the time periods
    """
    def timeIntersection(self, seqA, seqB):
        # Write your code here
        
        event = collections.defaultdict(int)
        for seq in seqA+seqB:
            event[seq.start] += 1
            event[seq.end] -= 1
            
        prevcount, count = 0, 0
        res = []
        start, end = 0, 0
        for ts in sorted(event.keys()):
            count += event[ts]
            if count == 2:
                start = ts
            elif prevcount == 2 and count < 2:
                end = ts
                res.append(Interval(start, end))
            prevcount = count
            
        return res