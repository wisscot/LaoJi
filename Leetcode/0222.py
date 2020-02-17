# 222. Count Complete Tree Nodes
'''
Given a complete binary tree, count the number of nodes.

Note:

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.
'''

Basic idea: DC

count of left/right children nodes + itself = 2**(child depth)


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
            
        Ldepth = self.depthof(root.left)
        Rdepth = self.depthof(root.right)
        if Ldepth == Rdepth:
            return 2**Ldepth + self.countNodes(root.right)
        return 2**Rdepth + self.countNodes(root.left)
        
    def depthof(self, root):
        res = 0
        while root:
            res += 1
            root = root.left
        return res