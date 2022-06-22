class Solution:
    def flatten(self, root: TreeNode) -> None:
        if not root:
            return None
        
        stack = [root]
        prev = None
        
        while stack:
            
            node = stack.pop()
            if node:
                stack.append(node.right)
                stack.append(node.left)
                
                if prev:
                    prev.right = node
                    prev.left = None
                    node.left = None
            
                prev = node