# Segment Tree


## 1. Good for single point update, range query

* build: Has to include all __Sorted and Unique__ nums waiting for update\
  Time O(n) space O(n)
  
* update: time Has to be an existing leaf node \
  Time O(logn)  

* query: Any range \
  Time O(logn)   
  

```python
class SegTree:
    # build the tree in __init__
    # assume nums sorted
    def __init__(self, start_i, end_i, nums):
        self.start, self.end = nums[start_i], nums[end_i]
        self.count = 0
        self.left, self.right = None, None
        if start_i < end_i:
            mid = (start_i+end_i)//2
            self.left = SegTree(start_i, mid, nums)
            self.right = SegTree(mid+1, end_i, nums)
            
    @classmethod
    def update(cls, root, val):
        if not root:
            return
        if root.start <= val <= root.end:
            root.count += 1 # preorder update, sum -> increment, min/max needs postorder
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

TAG
[315. Count of Smaller Numbers After Self](https://leetcode.com/problems/count-of-smaller-numbers-after-self/)
0209G Done

[327. Count of Range Sum](https://leetcode.com/problems/count-of-range-sum/)

[493. Reverse Pairs](https://leetcode.com/problems/reverse-pairs/)


## 2. Range update, single point query (Not recommend)

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

__Lazy propagation:__ 
if current node range was covered by todo range, then update the current node, update the lazy val of children

__Example:__

[218. The Skyline Problem](https://leetcode.com/problems/the-skyline-problem/)
\
better use sweepLine algorithm



