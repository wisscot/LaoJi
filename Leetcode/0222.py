# 222. Count Complete Tree Nodes
'''
Given a complete binary tree, count the number of nodes.

Note:

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.
'''

Basic idea: DC

count of left/right children nodes + itself = 2**(child depth)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        
        if root is None:
            return 0
        
        leftdepth = self.depth(root.left)
        rightdepth = self.depth(root.right)
        
        if leftdepth == rightdepth:
            return 2**leftdepth + self.countNodes(root.right)
        else:
            return 2**rightdepth + self.countNodes(root.left)
        
    def depth(self, root):
        res = 0
        while root:
            res += 1
            root = root.left
        return res