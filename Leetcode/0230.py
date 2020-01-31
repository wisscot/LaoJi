# 230. Kth Smallest Element in a BST

'''
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.
'''

Basic idea:
inorder traverse of a BST is a sorted list

Solution 1:
inorder traverse with generator (python only)

Solution 2:
inorder traverse with stack (iterative)
becomes 173. BST Iterator 

Solution 3: 
inorder traverse and save all nums in a list (not recommend)


Solution 1,2 time: O(k) average, O(n) worst
Solution 3 time: O(n)

# Solution 1: with generator (python only)
def generator(root):
    if root.left:
        yield from generator(root.left)
        
    yield root.val
    
    if root.right:
        yield from generator(root.right)

class Solution:
    """
    @param root: the given BST
    @param k: the given k
    @return: the kth smallest element in BST
    """
    def kthSmallest(self, root, k):
        # write your code here
        gen = generator(root)
        for _ in range(k):
            num = next(gen)
        return num
        