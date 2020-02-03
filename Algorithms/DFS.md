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
    path.pop() # backtracking
```
Time Complexity: O(num of solutions * time to construct a solution)

## Application

* find all possible solutions


## Examples

[39. Combination Sum](https://leetcode.com/problems/combination-sum/)
\
typical backtracking

[Lint10. String Permutation II](https://www.lintcode.com/problem/string-permutation-ii/description)

[Lint90. k Sum II](https://www.lintcode.com/problem/k-sum-ii/description)

