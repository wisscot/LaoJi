# Sweep Line

## Good for interval problems

Such as meeting rooms, sheduler, interval intersection, interval empty, etc.

Step 1. get all key events timestamp/position (remove duplicate)
\
Step 2. save events to dictionary, use event timestamp/position as key
\
Step 3. go over all unique timestamps, process and finally get result


__Examples:__

[Number of Airplanes in the Sky](https://www.lintcode.com/problem/number-of-airplanes-in-the-sky/description?_from=ladder&&fromId=106)  \
typical line sweep 

[218. The Skyline Problem](https://leetcode.com/problems/the-skyline-problem/)  
\
line sweep with hashheap (needs removal) or without
\
segment tree

[Time Intersection](https://www.lintcode.com/problem/time-intersection/description?_from=ladder&&fromId=106)
\
similar idea to plane in the sky problem, just count how many planes in the sky 0/1 -> 2 or 2 -> 0/1 \

[253. Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/)
\
same idea, max of number of planes in the sky





