# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        def get_sum(root):
            nonlocal ans
            
            if not root:
                return
            
            if low <= root.val <= high:
                ans += root.val
            
            get_sum(root.left)
            
            get_sum(root.right)
        
        ans = 0
        get_sum(root)
        return ans