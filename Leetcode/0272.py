# 272. Closest Binary Search Tree Value II

'''
Given a non-empty binary search tree and a target value, find k values in the BST that are closest to the target.

Note:

Given target value is a floating point.
You may assume k is always valid, that is: k ≤ total nodes.
You are guaranteed to have only one unique set of k values in the BST that are closest to the target.
'''

Basic idea:
Binary Search Tree iterative inorder traversal
Step 1. get the stack close node from root to leaf
Step 2. like two pointers get k close value
        move upperstack upper and lowerstack lower
Time: O(h + k)

An trivial solution: 
get all numbers inorder, then use binary search and two pointers
Time: O(n)

# Solution O(h+k)
class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @param k: the given k
    @return: k values in the BST that are closest to the target
    """
    def closestKValues(self, root, target, k):
        # write your code here
        if not root or k == 0:
            return []
            
        lowerstack = self.getstack(root, target)
        upperstack = list(lowerstack)
        
        if lowerstack[-1].val > target:
            self.movelower(lowerstack)
        else:
            self.moveupper(upperstack)
        
        res = []
        for i in range(k):
            if self.is_lower_closer(lowerstack, upperstack, target):
                res.append(lowerstack[-1].val)
                self.movelower(lowerstack)
            else:
                res.append(upperstack[-1].val)
                self.moveupper(upperstack)
                
        return res
        
    def getstack(self, root, target):
        res = []
        while root:
            res.append(root)
            if target > root.val:
                root = root.right
            else:
                root = root.left
        return res
        
    def moveupper(self, stack):
        # do not pop first
        # leave node in stack if it has right not visited
        # will be used as parent
        if stack[-1].right:
            node = stack[-1].right
            while node:
                stack.append(node)
                node = node.left
        else:
            node = stack.pop()
            while stack and stack[-1].right == node:
                node = stack.pop()
                
    def movelower(self, stack):
        # reverse left <-> right because its symmetric
        if stack[-1].left:
            node = stack[-1].left
            while node:
                stack.append(node)
                node = node.right
        else:
            node = stack.pop()
            while stack and stack[-1].left == node:
                node = stack.pop()

    def is_lower_closer(self, lowerstack, upperstack, target):
        if not lowerstack:
            return False
        
        if not upperstack:
            return True
            
        return target - lowerstack[-1].val <= upperstack[-1].val - target
                
    
        

