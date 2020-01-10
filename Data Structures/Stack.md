# Stack

##  Regular stack

* Convert recursive way to iterative way

__Examples:__

[155. Min Stack](https://leetcode.com/problems/min-stack/)\
use an extra stack to store corresponding min

[394. Decode String](https://leetcode.com/problems/decode-string/)\
recursive is trivial, use iterative to understand stack used in recursive


## Monotonous stack

* used to find the first item greater or smaller in the left and right side in an array

* Time O(n)

__Examples:__

[84. Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/)\
a typical mono stack problem

[85. Maximal Rectangle](https://leetcode.com/problems/maximal-rectangle/)\
can be solved based on #84

[654. Maximum Binary Tree](https://leetcode.com/problems/maximum-binary-tree/)\
found the need to find first greater element in left and right