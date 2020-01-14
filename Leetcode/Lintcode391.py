# 391. Number of Airplanes in the Sky

'''
Given an list interval, which are taking off and landing time of the flight. How many airplanes are there at most at the same time in the sky?

Example
Example 1:

Input: [(1, 10), (2, 3), (5, 8), (4, 7)]
Output: 3
Explanation:
The first airplane takes off at 1 and lands at 10.
The second ariplane takes off at 2 and lands at 3.
The third ariplane takes off at 5 and lands at 8.
The forth ariplane takes off at 4 and lands at 7.
During 5 to 6, there are three airplanes in the sky.
Example 2:

Input: [(1, 2), (2, 3), (3, 4)]
Output: 1
Explanation: Landing happen before taking off.
'''

Basic idea:
focus on the key points, which is the takeoff and touchdown points,
other wise the number of flights in the air won't change

Solution 1:
for every key points, loop the array to find how many planes 
Time O(n^2)

Solution 2: (recommend)
sort the key events, and loop through it 
when encount take off event, count+1, 
when encount touchdown event, count-1
record the max
0               10
    2    6
             8       12
^   ^    ^   ^  ^    ^
+   +    -   +  -    -
1   2    1   2  1    0 
note: since the interval e.g 2 to 6 is left inclusive and right exclusive,
      so same time takeoff and touchdown will be counted as touchdown first,
      so we need to sort touchdown before takeoff for same time event
Time: O(nlogn)  sorting donimates

Solution 3:
Segment Tree


class Solution:
    """
    @param airplanes: An interval array
    @return: Count of airplanes are in the sky.
    """
    def countOfAirplanes(self, airplanes):
        # write your code here
        keytimes = []
        for airplane in airplanes:
            keytimes += [(airplane.start,1), (airplane.end,0)]
            
        res, count = 0, 0
        for _, takeoff in sorted(keytimes):
            if takeoff:
                count += 1
            else:
                count -= 1
            res = max(res, count)
            
        return res