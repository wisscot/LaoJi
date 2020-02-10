# Heap / Priority Queue


## Overview 

Heap queue (Priority queue) doesnot support remove, while Heap supports

Time Complexity:
* Get min/max  __O(1)__

* Update  __O(logn)__

* Remove min/max  __O(logn)__

* Building (bottom up / sip down) __O(n)__

* Remove any __O(n)__


## Application

* Get min/max with removal online 

* Get kth largest online

* Get median online


## Merge K sorted arrs / liked list

- Solution 0: Brute Force   \
  Time O(nlogn) where n is the total number of nodes

- Solution 1: Use merge two sorted lists which takes O(n)   \
  merge every two for each layer    \
  Time O(nlogk)

- Solution 1+: Use merge two sorted lists which takes O(n)  \
  Divide and Conquer (top down) \
  Time O(nlogk)

- Solution 2: Heapq \
  Time: O(nlogk)


__Examples:__

[23. Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)
0210F \
3 solutions 

[264. Ugly Number II](https://leetcode.com/problems/ugly-number-ii/)

[378. Kth Smallest Element in a Sorted Matrix](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/)\
either start from a point or from a line

[Lint465. Kth Smallest Sum In Two Sorted Arrays](https://www.lintcode.com/problem/kth-smallest-sum-in-two-sorted-arrays/)\
based on the solution above

[Lint543. Kth Largest in N Arrays](https://www.lintcode.com/problem/kth-largest-in-n-arrays/)\
typical heap usage

TAG
[295. Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/)    
0201G\
with min heap and max heap

[480. Sliding Window Median](https://leetcode.com/problems/sliding-window-median/) \
similar to 295 but harder, requires implementing heap with remove (hashheap)  __TODO__

[407. Trapping Rain Water II](https://leetcode.com/problems/trapping-rain-water-ii/) \
barrel principle

TAG
[42. Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)\
1D version of trapping rain water, don't need heap, use two pointers or mono stack

