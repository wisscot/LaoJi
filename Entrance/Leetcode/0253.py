253. Meeting Rooms II

Basic idea: how many planes in the sky (sweep line)


"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def minMeetingRooms(self, intervals):
        # Write your code here
        
        events = []
        for itv in intervals:
            events += [(itv.start,1), (itv.end,0)]
        
        res, count = 0, 0
        for ts, sig in sorted(events):
            if sig:
                count += 1
            else:
                count -= 1
            res = max(res, count)
            
        return res