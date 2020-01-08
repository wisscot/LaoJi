# Segment Tree

## 1. Good for single point update, range query

* build: time O(n) space O(n)
* update: time O(logn)
* query: time O(logn)

```python
class SegTree:
    # build the tree in __init__
    def __init__(self, start_i, end_i, nums):
        self.start, self.end = nums[start_i], nums[end_i]
        self.left, self.right = None, None
        self.count = 0
        if start_i < end_i:
            mid = (start_i+end_i)//2
            self.left = SegTree(start_i, mid, nums)
            self.right = SegTree(mid+1, end_i, nums)
            
    @classmethod
    def update(cls, root, val):
        if not root:
            return
        if root.start <= val <= root.end:
            root.count += 1
            cls.update(root.left, val)
            cls.update(root.right, val)
            
    @classmethod
    def query(cls, root, start, end):
        if start <= root.start <= root.end <= end:
            return root.count
        if start > root.end or end < root.start:
            return 0
        return cls.query(root.left, start, end) + cls.query(root.right, start, end)     
```

__Example:__

[315. Count of Smaller Numbers After Self](https://leetcode.com/problems/count-of-smaller-numbers-after-self/)
[327. Count of Range Sum](https://leetcode.com/problems/count-of-range-sum/)
[493. Reverse Pairs](https://leetcode.com/problems/reverse-pairs/)


## 2. range update, single point query (for offline data)


By default:
* build: time O(N) space O(N)
* update: time O(N)
* query: time O(logN)
where N is the range of the number

applying range compression:
* build: time O(n) space O(n)
* update: time O(n)
* query: time O(logn)

applying Lazy propagation:
* update: time O(logn)

### Lazy propagation
if current node range was covered by todo range, then update the current node, update the lazy val of children

__Example:__

[218. The Skyline Problem](https://leetcode.com/problems/the-skyline-problem/)

