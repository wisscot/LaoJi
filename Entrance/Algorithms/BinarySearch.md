# Binary Search

__Template:__
```python
while left < right - 1:
    mid = (left+right) // 2
    if check(mid): # assume find a smaller val
        right = mid
    else:
        left = mid

if check(left): # check left and right separately
    return left
return right
```

## Binary Search on array

Python module: bisect
* bisect.bisect_left(nums, val)
* bisect.bisect_right(nums, val)
* bisect.insort_left(nums, val)
* bisect.insort_right(nums, val)

nums is assumed to be sorted\
target = 3

| [ | 1, | 2, | 3, | 3, | 3, | 4 | ] |
|---|----|----|----|----|----|---|---|
|   |    |    | ^  |    |    | ^ |   |
|   |    |    | L  |    |    | R |   |

* bisect_left returns the first accurance (left insert position)

* bisect_right returns the next of last accurance (right insert position)

* If target not exists, then bisect_left and bisect_right return the same.

```python
# Tips: Bisect alwasy returns equal or greater position, 
#       to find the number equal or less position, use
bisect.bisect_left(nums, val+1) - 1
```

__Examples:__

[704. Binary Search](https://leetcode.com/problems/binary-search/)
Easy 2024*2

[153. Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)
Medium 2020 2024
if not distint number, proved no O(logn) algorithm exists, such as [1,1,1,1,0,1,1,1,1,1,1]

[33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)
Medium 2020 2024

[162. Find Peak Element](https://leetcode.com/problems/find-peak-element/)
Medium 2020 2024

TAG
[1146. Snapshot Array](https://leetcode.com/problems/snapshot-array/)
0306F again



## Binary Search on result

Good for a problem that is easy to verify a proposed solution is correct or not, \
and the result must have a upper bound and lower bound


__Examples:__

[69. Sqrt(x)](https://leetcode.com/problems/sqrtx/)
Hard 2020 2024
typical binary search on result

[Lint183. Wood Cut](https://www.lintcode.com/problem/wood-cut/description?_from=ladder&&fromId=106)
Hard 2020 2024

[Lint437. Copy Books](https://www.lintcode.com/problem/copy-books/description?_from=ladder&&fromId=106)
Medium 2020 2024

[Lint438. Copy Books II](https://www.lintcode.com/problem/copy-books-ii/?_from=ladder&&fromId=106)
Locked 2020
Similar to Copy Books

[287. Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/)
Midium 2020 2024
Two solutions

[644. Maximum Average Subarray II](https://leetcode.com/problems/maximum-average-subarray-ii/)
0128F again\
Typical Binary search on result

[410. Split Array Largest Sum](https://leetcode.com/problems/split-array-largest-sum/)

[1011. Capacity To Ship Packages Within D Days](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/)
0207G, Done

[1231. Divide Chocolate](https://leetcode.com/problems/divide-chocolate/)
Similar to 410, Binary Search or DP

[Lint586. Sqrt(x) II](https://www.lintcode.com/problem/sqrtx-ii/description?_from=ladder&&fromId=106)
Locked 2020 
binary search on result on decimal
