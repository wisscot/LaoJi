# Two Pointers

## Forwards two pointers

On arrays:

master pointer i - for loop
\
slave pointer j - while loop

Algorithm:
  1. move j (while we should include element j)
  2. save result (arr[i:j])
  3. move i (outer for loop)

Time O(n)

On single linked list:\
Find loop / find location with slow/fast pointers


__Examples:__

[209. Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/)

[3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
0213G \

[159. Longest Substring with At Most Two Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/)
0213G \

[76. Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)
0213G \

[75. Sort Colors](https://leetcode.com/problems/sort-colors/)
\
challenge - sort into lt, eq, gt three parts

[Lint143. Sort Colors II](https://www.lintcode.com/problem/sort-colors-ii/description)



## Towards two pointers

On array:

i, j are moving simutanouly from two ends

Algorithm:
  1. i, j = 0, len - 1
  2. move i or j by 1
  3. save result e.g. count = j - i


__Examples:__

[125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)
0201G \
[680. Valid Palindrome II](https://leetcode.com/problems/valid-palindrome-ii/)
0201G \

TAG
[1. Two Sum](https://leetcode.com/problems/two-sum/) 
0218G \
mutiple solutions

[Lint609. Two Sum - Less than or equal to target](https://www.lintcode.com/problem/two-sum-less-than-or-equal-to-target/)

[Lint31. Partition Array](https://www.lintcode.com/problem/partition-array/description)

[611. Valid Triangle Number](https://leetcode.com/problems/valid-triangle-number/)  
0201F 0202F 0214G\
use large edge as master pointer

[16. 3Sum Closest](https://leetcode.com/problems/3sum-closest/)
\
convert to 2sum closest

[163. Missing Ranges](https://leetcode.com/problems/missing-ranges/) 
\
only one pointer is needed

[674. Longest Continuous Increasing Subsequence](https://leetcode.com/problems/longest-continuous-increasing-subsequence/)
\
Easy. Challedge: elegant

