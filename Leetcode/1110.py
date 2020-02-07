# 1110. Delete Nodes And Return Forest

'''
Given the root of a binary tree, each node in the tree has a distinct value.

After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).

Return the roots of the trees in the remaining forest.  You may return the result in any order.
'''

Basic idea: Recursion


class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        
        self.new_roots = []
        self.search(root, to_delete, 0)
        print([node.val for node in self.new_roots])
        return self.new_roots
    
    def search(self, root, to_delete, has_parent):
        
        if root is None:
            return 
        
        if root.val in to_delete:
            self.search(root.left, to_delete, 0)
            self.search(root.right, to_delete, 0)
            return
        
        if not has_parent:
            self.new_roots.append(root)
            
        self.search(root.left, to_delete, 1)        
        self.search(root.right, to_delete, 1)
        
        if root.left and root.left.val in to_delete:
            root.left = None
        if root.right and root.right.val in to_delete:
            root.right = None