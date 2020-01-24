# 173. Binary Search Tree Iterator
'''
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.
'''

Basic idea:
In-order traverse
put everything at the root left side to a stack, the last one is the next
then get its right, repeat above


class BSTIterator:
    """
    @param: root: The root of binary tree.
    """
    def __init__(self, root):
        # do intialization if necessary
        self.stack = []
        node = root
        while node:
            self.stack.append(node)
            node = node.left

    """
    @return: True if there has next node, or false
    """
    def hasNext(self):
        # write your code here
        return self.stack

    """
    @return: return next node
    """
    def next(self):
        # write your code here
        curr = self.stack.pop()
        
        node = curr.right
        while node:
            self.stack.append(node)
            node = node.left
                
        return curr