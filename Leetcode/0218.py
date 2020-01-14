218. The Skyline Problem

Basic idea:
The only positions will change height (need output) are within those start and end of buildings (key positions)
The skyline are basical the max height for every position
so the problem became checking if the max height changes at those key positions

Below are mutiple ways to get maximum height at those positions


Solution 0: Brute force
check height at a position by looping over all buildings,  (Time O(n^2))
see if its the same as the one to the left


Solution 1: Line Sweep with heapq

lets use pin to denote the top left corner of a building and use a heap for max height
when we encounter a key poistion,
we remove all pins that ends at this position and
we add all pins that starts at this position,
then we can get the max height at this position

The removal in heapq is O(n), so overall time is O(n^2), can be improved with hashheap

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        
        end_pins = collections.defaultdict(list)
        start_pins = collections.defaultdict(list)
        keypos = [] # unique
        
        for start, end, height in buildings:            
            pin = (-height, start) #pin is always (height, start)
            end_pins[end].append(pin)
            start_pins[start].append(pin)
            keypos += [start, end]
            
        keypos = sorted(set(keypos))

        hq = []
        prevheight = 0
        res = []
        for pos in keypos:
            
            # remove all building pins end at this position
            for pin in end_pins[pos]:
                hq.remove(pin) #todo
                heapq.heapify(hq) #todo
                # the time complexity to remove in heapq in O(n)
                # we need to implement our own heap to achieve O(logn)
                # build a HashHeap
            
            # add all building pins start at this position
            for pin in start_pins[pos]:
                heapq.heappush(hq, pin)
                
            height = -hq[0][0] if hq else 0
                
            if height != prevheight:
                res.append([pos, height])
                prevheight = height
                
        return res


Solution 1 - Improve 1: use hashheap for removal


Solution 1 - Improve 2: no need for hashheap

actually we dont have to delete every pin that ends at current position,
we only need to remove the ones that is higher than current max,
so the problem becomes remove the items which should be discarded from the heap,
that is - heap top one's end position <= current position
so we need to update the pin to include end -> (-height, start, end)

        ...
        for start, end, height in buildings:            
            pin = (-height, start, end)

        ...
        for pos in keypos:
            # remove higher building pins end at this position
            while hp and hp[0][2]<= pos:
                heapq.heappop(hp)



Solution 2:
with Segment Tree
Time: O(n*N) where n is the number of the building and N is the range of the x

class SegTree:
    def __init__(self, start, end):
        self.start, self.end, self.val = start, end, 0
        self.left, self.right = None, None
        if start < end:
            mid = (start+end) // 2
            self.left = SegTree(start, mid)
            self.right = SegTree(mid+1, end)
        
    @classmethod
    def update(cls, root, start, end, val):
        if root.start > end or root.end < start:
            return
        if root.start == root.end:
            root.val = max(root.val, val)
            return
        cls.update(root.left, start, end, val)
        cls.update(root.right, start, end, val)
        root.val = max(root.left.val, root.right.val)
        
    @classmethod
    def query(cls, root, x):
        if root.start == root.end == x:
            return root.val
        mid = (root.start+root.end)//2
        if x<=mid:
            return cls.query(root.left, x)
        return cls.query(root.right, x)
        
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        if not buildings:
            return []
        self.buildings = buildings
        key_points_x = []
        for building in buildings:
            key_points_x.append(building[0])
            key_points_x.append(building[1])
        key_points_x = sorted(set(key_points_x))
        self.root = SegTree(min(key_points_x)-1, max(key_points_x))
        for building in buildings:
            SegTree.update(self.root, 
                           building[0], 
                           building[1]-1, 
                           building[2])
        res = []
        for x in key_points_x:
            if self.is_flat(x):
                continue
            res.append([x, self.max_y_at(x)])
            
        return res
    
    def is_flat(self, x):
        if x == 0:
            return False
        return self.max_y_at(x) == self.max_y_at(x-1)
    
    def max_y_at(self, x):
        return SegTree.query(self.root, x)
        

Solution 2 - Improve 1: range compression
still TLE on last test case
Time: O(n^2)

class SegTree:
    def __init__(self, start, end):
        self.start, self.end, self.val = start, end, 0
        self.left, self.right = None, None
        if start < end:
            mid = (start+end) // 2
            self.left = SegTree(start, mid)
            self.right = SegTree(mid+1, end)
        
    @classmethod
    def update(cls, root, start, end, val):
        if root.start > end or root.end < start:
            return
        if root.start == root.end:
            root.val = max(root.val, val)
            return
        cls.update(root.left, start, end, val)
        cls.update(root.right, start, end, val)
        root.val = max(root.left.val, root.right.val)
        
    @classmethod
    def query(cls, root, x):
        if root.start == root.end == x:
            return root.val
        mid = (root.start+root.end)//2
        if x<=mid:
            return cls.query(root.left, x)
        return cls.query(root.right, x)
        
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        if not buildings:
            return []
        self.buildings = buildings
        key_points_x = []
        for building in buildings:
            key_points_x.append(building[0])
            key_points_x.append(building[1])
        key_points_x = sorted(set(key_points_x))
        mapping_x = {v:i for i,v in enumerate(key_points_x)}
        self.root = SegTree(0, len(key_points_x)-1)
        for building in buildings:
            SegTree.update(self.root, 
                           mapping_x[building[0]], 
                           mapping_x[building[1]]-1, 
                           building[2])
        res = []
        for i in range(len(key_points_x)):
            if self.is_flat(i):
                continue
            res.append([key_points_x[i], self.max_y_at(i)])
            
        return res
    
    def is_flat(self, x):
        if x == 0:
            return False
        return self.max_y_at(x) == self.max_y_at(x-1)
    
    def max_y_at(self, x):
        return SegTree.query(self.root, x)


Solution 2 - Improve 2: Seg Tree Lazy Propagation
O ( n * logn)
https://www.youtube.com/watch?v=xuoQdt5pHj0&t=920s

class SegTree:
    def __init__(self, start, end):
        self.start, self.end, self.val = start, end, 0
        self.left, self.right = None, None
        self.lazy = 0
        if start < end:
            mid = (start+end) // 2
            self.left = SegTree(start, mid)
            self.right = SegTree(mid+1, end)
            
    @classmethod
    def lazy_prop(cls, root):
        if not root or root.lazy == 0:
            return
        root.val = max(root.val, root.lazy)
        if root.left:
            root.left.lazy = max(root.left.lazy, root.lazy)
            root.right.lazy = max(root.right.lazy, root.lazy)
        root.lazy = 0
        
    @classmethod
    def update(cls, root, start, end, val):
        cls.lazy_prop(root)
        if root.start > end or root.end < start:
            return
        if start<=root.start <= root.end<=end:
            root.val = max(root.val, val)
            if root.left:
                root.left.lazy = max(root.left.lazy, val)
                root.right.lazy = max(root.right.lazy, val)
            return
        cls.update(root.left, start, end, val)
        cls.update(root.right, start, end, val)
        root.val = max(root.left.val, root.right.val)
        
    @classmethod
    def query(cls, root, x):
        cls.lazy_prop(root)        
        if root.start == root.end == x:
            return root.val
        mid = (root.start+root.end)//2
        if x<=mid:
            return cls.query(root.left, x)
        return cls.query(root.right, x)
        
        
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        if not buildings:
            return []
        self.buildings = buildings
        key_points_x = []
        for building in buildings:
            key_points_x.append(building[0])
            key_points_x.append(building[1])
        key_points_x = sorted(set(key_points_x))
        mapping_x = {v:i for i,v in enumerate(key_points_x)}
        self.root = SegTree(0, len(key_points_x)-1)
        for building in buildings:
            SegTree.update(self.root, 
                           mapping_x[building[0]], 
                           mapping_x[building[1]]-1, 
                           building[2])
        res = []
        for i in range(len(key_points_x)):
            if self.is_flat(i):
                continue
            res.append([key_points_x[i], self.max_y_at(i)])
            
        return res
    
    def is_flat(self, x):
        if x == 0:
            return False
        return self.max_y_at(x) == self.max_y_at(x-1)
    
    def max_y_at(self, x):
        return SegTree.query(self.root, x)
        