# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        max_sum = float('-inf')

        def pathSum(root):
            nonlocal max_sum
            if not root:
                return 0
            
            # trick
            # if negative return 0
            # limit the answer to root
            # we want to maximize the sum
            left = max(0, pathSum(root.left))
            right = max(0, pathSum(root.right))
            
            max_sum = max(max_sum, left+right+root.val)
            
            return root.val + max(left, right)
        
        pathSum(root)
        return max_sum
            