# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        
        def solve(root):
            nonlocal res
            if not root or not res:
                return 0

            left_height = solve(root.left)
            right_height = solve(root.right)
            
            if abs(left_height - right_height) > 1:
                res = False
            
            return 1+max(left_height, right_height)
        
        res = True
        solve(root)
        return res