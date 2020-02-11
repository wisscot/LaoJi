# Stack & Queue

##  Regular stack

* Convert recursive way to iterative way

* Deal with data when encouting induced point, e.g. ']' in 394  \
  before that, just push to stack blindly

__Examples:__

[155. Min Stack](https://leetcode.com/problems/min-stack/)
0211F \
use an extra stack to store corresponding min

[394. Decode String](https://leetcode.com/problems/decode-string/)
0211F again\
recursive is trivial, use iterative to understand stack used in recursive

Calculator I, II, III, IV\
[227. Basic Calculator II](https://leetcode.com/problems/basic-calculator-ii/)
0211G \
operations include + - * / \
for parensis () just add a recursion

[150. Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/)
0211F \
easy with stack, but be careful with details

[251. Flatten 2D Vector](https://leetcode.com/problems/flatten-2d-vector/)
0211G \
Iterator

[173. Binary Search Tree Iterator](https://leetcode.com/problems/binary-search-tree-iterator/)
0211G \
Iterator


## Monotonous stack

* used to find the first item greater or smaller in the left and right side in an array

* Shall we use incresing mono stack or decresing mono stack?
  - we __calculate current node based result when stack pop__
  - so, e.g. LC84 need find left and right first smaller one, when meet the smaller it will pop

* Time O(n)

__Examples:__

[84. Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/)
0210G\
a typical mono stack problem

[85. Maximal Rectangle](https://leetcode.com/problems/maximal-rectangle/)
0211F\
can be solved based on #84

[654. Maximum Binary Tree](https://leetcode.com/problems/maximum-binary-tree/)\
0211F again\
Difficult to think


## Monotonous queue

__Examples:__

[239. Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/)
0211G \
with heap, similar to skyline problem\
or with monotonous queue
