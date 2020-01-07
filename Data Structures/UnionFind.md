# Union Find
Good for
> Used to check connectivity in Graph (online)
check, query, check, query ... 



> Find with path compression
> Union by rank is optional

Data stored in array or dict

```python
class UnionFind:
    def __init__(self, n):
        self.p = list(range(n))

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            self.p[rootx] = rooty
            # self.numBlock -= 1
```


__Example:__
[305. Number of Islands II](https://leetcode.com/problems/number-of-islands-ii/)

[261. Graph Valid Tree](https://leetcode.com/problems/graph-valid-tree/)

[721. Accounts Merge](https://leetcode.com/problems/accounts-merge/)

