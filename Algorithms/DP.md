# Dynamic Programming

## Overview
Feelings: \
So easy to make mistake even using recursive way ... \
Have to be extremely careful

Step 1. Define entries in the table T(i) or T(i,j) \
Step 2. Recurrence for entries interms of smaller subproblem\
&emsp;  (thinking about the last step)\
&emsp;  T(i, j) =  T(i-1,j) if ... \
&emsp;&emsp; &emsp; = T(i, j-1) if ...\
Step 3. Base cases


## Space Optimization
O(mn) can sometimes reduced to O(n) as only two rows need\
             i-1,j-1   i-1,j
                     \  ^ 
             i,j-1   <  i,j

if its like 
             i-1,j-1   i-1,j
                        ^ 
             i,j-1   <  i,j
Then only 1d array is necessary by sweeping from left to right

if its like
             i-1,j-1   i-1,j
                     \   ^ 
             i,j-1      i,j
Then we can use 1d array to sweep from right to left



__Examples:__

[64. Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum/)

[91. Decode Ways](https://leetcode.com/problems/decode-ways/)

[Lint394. Coins in a Line](https://www.lintcode.com/problem/coins-in-a-line/)

[Lint395. Coins in a Line II](https://www.lintcode.com/problem/coins-in-a-line-ii/)
\
redo it 

[Lint396. Coins in a Line III](https://www.lintcode.com/problem/coins-in-a-line-iii/)
\
Interval

[312. Burst Balloons](https://leetcode.com/problems/burst-balloons/)
\
think from last step

[152. Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/)
\
use min max as states, redo it

[198. House Robber](https://leetcode.com/problems/house-robber/)

[674. Longest Continuous Increasing Subsequence](https://leetcode.com/problems/longest-continuous-increasing-subsequence/)
\
Difficulty: easy. Challedge: elegant

[1143. Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/)
\
typical

[72. Edit Distance](https://leetcode.com/problems/edit-distance/)

[97. Interleaving String](https://leetcode.com/problems/interleaving-string/)
\
can reduce one dimension

[Lint623. K Edit Distance](https://www.lintcode.com/problem/k-edit-distance/)
\
difficult, dp + dfs + trie

[Lint92. Backpack](https://www.lintcode.com/problem/backpack)\
[Lint125. Backpack II](https://www.lintcode.com/problem/backpack-ii/)\
[Lint440. Backpack III](https://www.lintcode.com/problem/backpack-iii/)\
\
original Backpack

[89. k Sum](https://www.lintcode.com/problem/k-sum/)

TAG 
[727. Minimum Window Subsequence](https://leetcode.com/problems/minimum-window-subsequence/)
0130F

TAG
[221. Maximal Square](https://leetcode.com/problems/maximal-square/)
0131P