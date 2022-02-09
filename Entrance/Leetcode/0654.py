# 654. Maximum Binary Tree

'''
Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

The root is the maximum number in the array.
The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
Construct the maximum tree by the given array and output the root node of this tree.
'''


Basic idea:
draw the tree, it can be found that 
each node s parent is the min{first one larger in the left, first one larger in the right}
-> "to find first greater element in left and right"
so, monotonous stack can be used to solve it

Time O(n)

# Solution MonoStack
class Solution:
    def maxTree(self, A):

        dummy = TreeNode(float('inf'))
        mono = [dummy]
        
        for a in A:
            curr = TreeNode(a)
            while mono and curr.val > mono[-1].val:
                prev = mono.pop()
                if mono[-1].val < curr.val:
                    mono[-1].right = prev
                else:
                    curr.left = prev
            mono.append(curr)
        
        for i in range(len(mono)-1):
            mono[i].right = mono[i+1]
            
        return dummy.right
        

# from Leetcode discussion
class Solution(object):
    def constructMaximumBinaryTree(self, arr):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        stack = []
        for num in arr:
            cur = TreeNode(num)
            while stack and stack[-1].val < cur.val:
                cur.left = stack.pop()
            if stack:
                stack[-1].right = cur 
            stack.append(cur)
        return stack[0]