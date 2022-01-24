# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        
        acc_sum = 0
        
        def solve(root):
            nonlocal acc_sum
            
            if not root:
                return 
            
            solve(root.right)
            
            old_val = root.val
            root.val += acc_sum
            acc_sum += old_val
            
            solve(root.left)
        
        solve(root)
        
        return root