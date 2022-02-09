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
0218G

[Lint396. Coins in a Line III](https://www.lintcode.com/problem/coins-in-a-line-iii/)
\
Interval

[312. Burst Balloons](https://leetcode.com/problems/burst-balloons/)
\
think from last step

[152. Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/)
0213F 0218G \
use min max as states

[198. House Robber](https://leetcode.com/problems/house-robber/)

[1143. Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/)
\
typical

[72. Edit Distance](https://leetcode.com/problems/edit-distance/)
0218G \

[97. Interleaving String](https://leetcode.com/problems/interleaving-string/)
\
can reduce one dimension

[Lint623. K Edit Distance](https://www.lintcode.com/problem/k-edit-distance/)
\
difficult, dp + dfs + trie

[Lint92. Backpack](https://www.lintcode.com/problem/backpack)\
[Lint125. Backpack II](https://www.lintcode.com/problem/backpack-ii/)\
[Lint440. Backpack III](https://www.lintcode.com/problem/backpack-iii/)\
original Backpack

[89. k Sum](https://www.lintcode.com/problem/k-sum/)

TAG 
[727. Minimum Window Subsequence](https://leetcode.com/problems/minimum-window-subsequence/)
0130F 0217G

TAG
[221. Maximal Square](https://leetcode.com/problems/maximal-square/)
0131G 0218G Done

TAG
[801. Minimum Swaps To Make Sequences Increasing](https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing/)

TAG
[1048. Longest String Chain](https://leetcode.com/problems/longest-string-chain/)

TAG
[552. Student Attendance Record II](https://leetcode.com/problems/student-attendance-record-ii/)

[1349. Maximum Students Taking Exam](https://leetcode.com/problems/maximum-students-taking-exam/)
\
DP + Bitmask

TAG
[300. Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/)
0218G \
two solutions, this is the basic for Russian Doll Envelopes