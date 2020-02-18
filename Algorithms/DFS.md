# Depth First Search

Also known as BackTracking

## Template

* Recursion Definition
* Recursion Exit
* Recursion BreakDown

```python
def search(nums, target, path, res):
    if should_exit:
        return
    
    if should_save_result:
        res.append(list(path))
        
    path.append(some value)
    self.search(next level)
    path.pop() # backtracking, NOT path.pop(val)
```
Time Complexity: O(num of solutions * time to construct a solution)

Think of of DFS as tree:
   * Each node is the search function
   * Search function parameters are the status of the node
   * Each edge represents the num/char (think about Trie)
   * Path stores all edges along the path
   * Draw the tree and figure out the status of the node and path, and exit condition before coding


## Application

* find all possible solutions


## Examples

[39. Combination Sum](https://leetcode.com/problems/combination-sum/)
0218F again\
typical backtracking

[Lint10. String Permutation II](https://www.lintcode.com/problem/string-permutation-ii/description)
0218F again\

[Lint90. k Sum II](https://www.lintcode.com/problem/k-sum-ii/description)

[51. N-Queens](https://leetcode.com/problems/n-queens/)

[17. Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)

[212. Word Search II](https://leetcode.com/problems/word-search-ii/)
\
DFS + Trie

[126. Word Ladder II](https://leetcode.com/problems/word-ladder-ii/)
\
BFS + DFS

TAG
[465. Optimal Account Balancing](https://leetcode.com/problems/optimal-account-balancing/)

TAG
[489. Robot Room Cleaner](https://leetcode.com/problems/robot-room-cleaner/)
0217G \
Real world DFS

TAG
[1219. Path with Maximum Gold](https://leetcode.com/problems/path-with-maximum-gold/)
0207G Done

TAG
[1088. Confusing Number II](https://leetcode.com/problems/confusing-number-ii/)
0208G \ 
Math and DFS