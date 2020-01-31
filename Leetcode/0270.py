# 270. Closest Binary Search Tree Value

'''
Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Note:

Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.
'''

Basic idea:
Go towards left/right depends on current node val

Time O(logn)

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        lower = upper = root.val
        
        while root:
            if root.val < target:
                upper = root.val
                root = root.right
            else:
                lower = root.val
                root = root.left
                
        if abs(lower-target) < abs(upper-target):
            return lower
        return upper
        
        