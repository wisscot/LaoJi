# Two Pointers

## Onwards two pointers


### Master on right, slave on left (prefer)

... | 1 2 3 4 1 | 2 3 ... 
      ^       ^
      i       j
    slave   Master
    |   valid   |  

```python
for j in range(n):
    include [j]
    while i should be excluded:
        res = j - i + 1 (shortest)
        i += 1
    res = j - i + 1  (longest)
```
Time O(n)


### Master on left, Slave on right (good for shortest)

... | 1 2 3 | 1 2 3 ... 
      ^       ^
      i       j
    Master  slave
    | valid |  


```python
for i in range(n):
    while [j] should be included:
        include [j]
        j += 1
    res = j - i
```
Time O(n)

> slave is lazy, so slave on right is good for shorest, slave on left is good for longest 

### On single linked list:
Find loop / find location with slow/fast pointers


__Examples:__

[209. Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/)
Medium 2020 2024

[3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
Medium 2020 2024

[76. Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)
Hard 2020 2024

[Topics: Sort](../Allgorithm-Topics/Sort.md)

[75. Sort Colors](https://leetcode.com/problems/sort-colors/)
Medium 2020 2024
challenge - one pass, constant space 

[Lint143. Sort Colors II](https://www.lintcode.com/problem/sort-colors-ii/description)
Medium 2020 2024
Quicksort variation 

[159. Longest Substring with At Most Two Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/)
Locked




## Towards two pointers

On array:

i, j are moving simutanouly from two ends

```python
i, j = 0, len(nums) - 1
res = 0
while i < j:
    if some condition:
        res += j - i
        i += 1
    else:
        j -= 1
# all logic are in if ... elif ... else, nothing outside
```

__Examples:__

[125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)
Easy 2020 2024*

[680. Valid Palindrome II](https://leetcode.com/problems/valid-palindrome-ii/)
Easy 2020 2024

[1. Two Sum](https://leetcode.com/problems/two-sum/) 
Easy 2020 2024
mutiple solutions

[Lint609. Two Sum - Less than or equal to target](https://www.lintcode.com/problem/two-sum-less-than-or-equal-to-target/)
Medium 2020 2024*

[611. Valid Triangle Number](https://leetcode.com/problems/valid-triangle-number/)  
Medium 2020 2024
use large edge as master pointer

[16. 3Sum Closest](https://leetcode.com/problems/3sum-closest/)
Medium 2020 2024
convert to 2sum closest

[674. Longest Continuous Increasing Subsequence](https://leetcode.com/problems/longest-continuous-increasing-subsequence/)
Easy 2020 2024
Easy. Challedge: elegant

[163. Missing Ranges](https://leetcode.com/problems/missing-ranges/) 
Locked
only one pointer is needed
