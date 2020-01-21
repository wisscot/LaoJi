# 297. Serialize and Deserialize Binary Tree


Solution 1: BFS
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
            
        res = []
        queue = collections.deque([root])
        while queue:
            head = queue.popleft()
            if head:
                res.append(str(head.val))
                queue.append(head.left)
                queue.append(head.right)
            else:
                res.append('#')
            
        while res and res[-1] == '#':
            res.pop()
            
        print(res)
        return ','.join(res)
        
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
            
        vals = collections.deque(data.split(','))
        root = TreeNode(int(vals.popleft()))
        queue = collections.deque([root])
        
        while queue:
            head = queue.popleft()
            if vals:
                left = vals.popleft()
                if left != '#':
                    head.left = TreeNode(int(left))
                    queue.append(head.left)
            if vals:
                right = vals.popleft()
                if right != '#':
                    head.right = TreeNode(int(right))
                    queue.append(head.right)
        return root
    
    
    # use two pointers deserialize
    def deserialize(self, data):
        # None or ""
        if not data:
            return None

        bfs_order = [
            TreeNode(int(val)) if val != '#' else None
            for val in data.split()
        ]
        root = bfs_order[0]
        fast_index = 1
        
        nodes, slow_index = [root], 0
        while slow_index < len(nodes):
            node = nodes[slow_index]
            slow_index += 1
            node.left = bfs_order[fast_index]
            node.right = bfs_order[fast_index + 1]
            fast_index += 2
            
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)
        
        return root    
        

Solution 2: Preorder traversal tree
    def serialize(self, root):
        if not root:
            return '#'
        return str(root.val)+','+self.serialize(root.left)+','+self.serialize(root.right) 
        
    def deserialize(self, data):
        vals = iter(data.split(','))
        def unpack():
            val = next(vals)
            if val == '#':
                return None
            root = TreeNode(int(val))
            root.left = unpack()
            root.right = unpack()
            return root
            
        return unpack()