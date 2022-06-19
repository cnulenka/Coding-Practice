# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        def path_sum(root):
            nonlocal max_sum
            if not root:
                return 0
            
            left_sum = max(0, path_sum(root.left))
            right_sum = max(0, path_sum(root.right))
            
            max_sum = max(max_sum, root.val + left_sum + right_sum)
            
            return root.val + max(left_sum, right_sum)
        
        
        max_sum = root.val
        path_sum(root)
        return max_sum