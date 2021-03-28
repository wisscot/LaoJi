# 257. Binary Tree Paths
'''
Given a binary tree, return all root-to-leaf paths.
Note: A leaf is a node with no children.
'''

Basic idea: 

Solution 1. DFS

Solution 2. DC

Note that its root to leaf

# Solution 1
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        res = []
        self.search(root, [], res)
        for i in range(len(res)):
            res[i] = '->'.join(map(str,res[i]))
        return res
    
    def search(self, root, path, res):
        
        path.append(root.val)
        if root.left is None and root.right is None:
            res.append(list(path))
            path.pop()
            return
            
        if root.left:
            self.search(root.left, path, res)
        if root.right:
            self.search(root.right, path, res)
        path.pop()