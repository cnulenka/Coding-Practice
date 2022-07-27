class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # pre order, root left right
        
        if not root:
            return 
        
        stack = [root]
        prev = None
        while stack:
            root = stack[-1]
            stack.pop()
            
            if prev:
                prev.right = root
            
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)
                root.left = None
            
            prev = root
            