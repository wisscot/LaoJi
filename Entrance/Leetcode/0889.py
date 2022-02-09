# 889. Construct Binary Tree from Preorder and Postorder Traversal

'''
Return any binary tree that matches the given preorder and postorder traversals.

Values in the traversals pre and post are distinct positive integers.

Example 1:

Input: pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]
Output: [1,2,3,4,5,6,7]
'''

Solution 1: DC
Time O(n^2)   (best O(n))

Solution 2: Iterative
Go through preorder vals, 
    append to stack
    if stack last node val == post order val,
    then it means the last node in the stack is complete, can pop out
when pop out, append that node to its parent, left preferred,
because the way to construct the tree is not unique,
e.g. pre=[1,2] post=[2,1], the node 2 could be left or right child of 1
Time O(n)


# Solution 1
def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
    if not pre:
        return None
    
    root = TreeNode(pre[0])
    if len(pre) == 1:
        return root
    
    j = pre.index(post[~1])
    root.left = self.constructFromPrePost(pre[1:j], post[:j-1])
    root.right = self.constructFromPrePost(pre[j:], post[j-1:-1])
    
    return root


# Solution 2
def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
    stack = []
    j = 0
    
    for i in range(len(pre)):
        
        node = TreeNode(pre[i]) 
        stack.append(node)
        
        while j < len(pre) and stack[-1].val == post[j]:
            root = stack.pop()
            j += 1
            if not stack:
                return root
            if stack[-1].left:
                stack[-1].right = root
            else:
                stack[-1].left = root
            
        
        


