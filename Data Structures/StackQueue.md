# Stack

##  Regular stack

* Convert recursive way to iterative way

__Examples:__

[155. Min Stack](https://leetcode.com/problems/min-stack/)\
use an extra stack to store corresponding min

[394. Decode String](https://leetcode.com/problems/decode-string/)\
recursive is trivial, use iterative to understand stack used in recursive

Calculator I, II, III, IV\
[227. Basic Calculator II](https://leetcode.com/problems/basic-calculator-ii/)\
operations include + - * / \
for parensis () just add a recursion

[150. Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/)\
easy with stack, but be careful with details

[251. Flatten 2D Vector](https://leetcode.com/problems/flatten-2d-vector/)
\
Iterator

[173. Binary Search Tree Iterator](https://leetcode.com/problems/binary-search-tree-iterator/)
\
Iterator


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

&nbsp;


# Deque

## Monotonous queue

__Examples:__

[239. Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/)
\
with heap, similar to skyline problem\
or with monotonous queue
