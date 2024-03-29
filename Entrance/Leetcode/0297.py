# 297. Serialize and Deserialize Binary Tree

'''
Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.
'''

Solution 1: BFS
Solution 2: DFS - preorder traversal

# Solution 1: BFS
class Codec:
    def serialize(self, root):
        res = []
        queue = collections.deque([root])
        
        while queue:
            node = queue.popleft()
            if node is None:
                res.append('#')
                continue
            res.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)
        
        return ','.join(res)
        
    # with deque + deque
    def deserialize(self, data):
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
    
    # with deque + iterator
    def deserialize(self, data):
        if data == '#':
            return None
        
        vals = iter(data.split(','))
        root = TreeNode(int(next(vals)))
        
        currlayer = collections.deque([root])
        while currlayer:
            for _ in range(len(currlayer)):
                node = currlayer.popleft()
                val = next(vals)
                node.left = TreeNode(int(val)) if val != '#' else None
                val = next(vals)
                node.right = TreeNode(int(val)) if val != '#' else None
                if node.left:
                    currlayer.append(node.left)
                if node.right:
                    currlayer.append(node.right)
                
        return root

    # with two pointers
    def deserialize(self, data):
        vals = data.split(',')
        nodes = [TreeNode(int(val)) if val != '#' else None for val in vals ]
        i, j = 0, 1
        while j < len(nodes):
            if nodes[i] is None:
                i += 1
                continue
            nodes[i].left = nodes[j]
            nodes[i].right = nodes[j+1]
            i += 1
            j += 2
        return nodes[0]
                 

# Solution 2: DFS 
# Preorder traversal tree
class Codec:
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