# Two Pointers

## Same-Direction

__Examples:__

[209. Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/)

[3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

[159. Longest Substring with At Most Two Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/)

* master pointer i - for loop
* slave pointer j - while loop
* Algorithm:
  1. move j (while we should include element j)
  2. save result (arr[i:j])
  3. move i (using for)
* Time O(n)

