# 114. Flatten Binary Tree to Linked List

'''
Given a binary tree, flatten it to a linked list in-place.
'''


class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def flatten(self, root):
        # write your code here
        self.flat(root)
        return root
        
    def flat(self, root): # return tail of tree of root
        if not root:
            return None
            
        lefttail = self.flat(root.left)
        righttail = self.flat(root.right)
        
        if lefttail:
            lefttail.right = root.right
            root.right = root.left
            root.left = None
        
        if righttail:
            return righttail
        if lefttail:
            return lefttail
        return root