# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, node: Optional[TreeNode]) -> str:
        
        res = ""
        
        def solve(root):
            nonlocal res
            
            if not root:
                return
            
            res += str(root.val)
            
            if not root.left and not root.right:
                return
            
            res +=  "("
            solve(root.left)
            res += ")"
            
            if root.right:
                res += "("
                solve(root.right)
                res += ")"
        
        solve(node)
        return res
        