# 173. Binary Search Tree Iterator
'''
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.
'''

Basic idea:
In-order traverse

Solution 1: 
put everything at the root left side to a stack, the last one is the next
then get its right, repeat above

Solution 2:
Python generator, next()

# Solution 1:
class BSTIterator:
    def __init__(self, root):
        self.stack = []
        node = root
        
    def hasNext(self):
        return self.stack

    def next(self):
        curr = self.stack.pop()
        
        node = curr.right
        while node:
            self.stack.append(node)
            node = node.left
                
        return curr
        

# Solution 2: 
def bst_gen(root):
    if root is None:
        return
    yield from bst_gen(root.left)
    yield root.val
    yield from bst_gen(root.right)
    
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.gen = bst_gen(root)
        self.nextval = next(self.gen, None)

    def next(self) -> int:
        val = self.nextval
        self.nextval = next(self.gen, None)
        return val

    def hasNext(self) -> bool:
        return self.nextval is not None
