# Heap / Priority Queue

## Overview 

* Get min/max in time O(1)
* Update in time O(logn)
* Remove min/max in time O(logn)
* Building (bottom up) in time O(n)

## Application

* Get min/max online with removal
* Get kth largest online
* Get median online

__Examples:__

[295. Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/)

[480. Sliding Window Median](https://leetcode.com/problems/sliding-window-median/) \
similar to 295 but harder, requires implementing heap with adding hash

[407. Trapping Rain Water II](https://leetcode.com/problems/trapping-rain-water-ii/)

[42. Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)\
1D version of trapping rain water, don't need heap, use two pointers or mono stack

