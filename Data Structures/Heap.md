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

[378. Kth Smallest Element in a Sorted Matrix](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/)\
either start from a point or from a line

[Kth Smallest Sum In Two Sorted Arrays](https://www.lintcode.com/problem/kth-smallest-sum-in-two-sorted-arrays/description?_from=ladder&&fromId=106)\
based on the solution above

[23. Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)\
todo, multiple solution

[Kth Largest in N Arrays](https://www.lintcode.com/problem/kth-largest-in-n-arrays/description?_from=ladder&&fromId=106)\
typical heap usage

TAG
[295. Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/)    \
with min heap and max heap

[480. Sliding Window Median](https://leetcode.com/problems/sliding-window-median/) \
similar to 295 but harder, requires implementing heap with remove (hashheap)  __TODO__

[407. Trapping Rain Water II](https://leetcode.com/problems/trapping-rain-water-ii/) \
barrel principle

TAG
[42. Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)\
1D version of trapping rain water, don't need heap, use two pointers or mono stack

