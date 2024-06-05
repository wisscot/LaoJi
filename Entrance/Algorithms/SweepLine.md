# Sweep Line

## Good for interval problems

Such as meeting rooms, sheduler, interval intersection, interval empty, etc.

Step 1. get all key events timestamp/position (remove duplicate)
\
Step 2. save events to dictionary, use event timestamp/position as key
\
Step 3. go over all unique timestamps, process and finally get result

## Template 
```python
time_events = build_time_events() 
# {ts1: [event1, event2, ...], ts2: [...], ...}

for ts in sorted(time_events.key()):
    process(time_events[ts])
```

__Examples:__

[Lint391. Number of Airplanes in the Sky](https://www.lintcode.com/problem/number-of-airplanes-in-the-sky/)
Medium 2020 2024
typical line sweep 

[218. The Skyline Problem](https://leetcode.com/problems/the-skyline-problem/)
Hard 2020 
line sweep with hashheap (needs removal) or without

[Lint821. Time Intersection](https://www.lintcode.com/problem/time-intersection/)
Locked
similar idea to plane in the sky problem, just count how many planes in the sky 0/1 -> 2 or 2 -> 0/1 \

[253. Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/)
Locked
same idea, max of number of planes in the sky

[1326. Minimum Number of Taps to Open to Water a Garden](https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/)
Hard 2020 
simplify it



