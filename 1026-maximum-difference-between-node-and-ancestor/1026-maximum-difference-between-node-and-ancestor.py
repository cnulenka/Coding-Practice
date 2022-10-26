# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        def solve(node, curr_max, curr_min):
            
            if not node: # end of path 
                return curr_max - curr_min
                
            curr_max = max(node.val, curr_max)
            curr_min = min(node.val, curr_min)
            
            left = solve(node.left, curr_max, curr_min)
            right = solve(node.right, curr_max, curr_min)
            
            return max(left, right)
        
        return solve(root, root.val, root.val)