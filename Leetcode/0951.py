# 951. Flip Equivalent Binary Trees

'''
For a binary tree T, we can define a flip operation as follows: choose any node, and swap the left and right child subtrees.

A binary tree X is flip equivalent to a binary tree Y if and only if we can make X equal to Y after some number of flip operations.

Write a function that determines whether two binary trees are flip equivalent.  The trees are given by root nodes root1 and root2.
'''

Basic idea: DC


class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        if root1 is root2:
            return True

        if not root1 or not root2 or root1.val != root2.val:
            return False

        return (self.flipEquiv(root1.left, root2.left) and \
                self.flipEquiv(root1.right, root2.right)) or \
               (self.flipEquiv(root1.left, root2.right) and \
                self.flipEquiv(root1.right, root2.left))


        