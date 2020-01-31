# 236. Lowest Common Ancestor of a Binary Tree

'''
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
'''

Basic idea: Binary Tree Traversal


# Solution 1: DC
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lca, _ = self.search(root, p, q)
        return lca
    
    def search(self, root, p, q):
        if root is None:
            return (None, 0)
        
        cnt = root == p or root == q
        leftlca, leftcnt = self.search(root.left, p, q)
        rightlca, rightcnt = self.search(root.right, p, q)
        
        if leftcnt == 2:
            return (leftlca, leftcnt)
        if rightcnt == 2:
            return (rightlca, rightcnt)
        
        currcnt = cnt + leftcnt + rightcnt
        if currcnt == 0:
            return (None, 0)
        else:
            return (root, currcnt)


# Solution 2: dfs get root->target path
# then compare two path
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        pathP = []
        pathQ = []
        
        self.dfs(root, p, [], pathP)
        self.dfs(root, q, [], pathQ)
        
        pathP = pathP[0]
        pathQ = pathQ[0]
        
        for node in pathP[::-1]:
            if node in pathQ:
                return node
    
    def dfs(self, root, target, path, res):
        if root is None:
            return
        
        path.append(root)
        if root == target:
            res.append(list(path))
        self.dfs(root.left, target, path, res)
        self.dfs(root.right, target, path, res)
        path.pop()