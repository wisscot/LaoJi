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
|   |    |    | l  |    |    | r |   |
bisect_left returns the first accurance\
bisect_right returns the next of last accurance\
if target not exists, then bisect_left and bisect_right return the same

## Binary Search on result

Good for a problem that is easy to verify a proposed solution is correct or not, \
and the result must have a upper bound and lower bound


__Examples:__

[69. Sqrt(x)](https://leetcode.com/problems/sqrtx/)
\
typical binary search on result

[Lint586. Sqrt(x) II](https://www.lintcode.com/problem/sqrtx-ii/description?_from=ladder&&fromId=106)
\
binary search on result on decimal

[Lint183. Wood Cut](https://www.lintcode.com/problem/wood-cut/description?_from=ladder&&fromId=106)

[Lint437. Copy Books](https://www.lintcode.com/problem/copy-books/description?_from=ladder&&fromId=106)

[Lint438. Copy Books II](https://www.lintcode.com/problem/copy-books-ii/?_from=ladder&&fromId=106)
\
Similar to I

[287. Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/)
\
Two solutions

[644. Maximum Average Subarray II](https://leetcode.com/problems/maximum-average-subarray-ii/)
worth do again\
Typical Binary search on result

