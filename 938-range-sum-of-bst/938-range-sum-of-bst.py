# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        summ = 0
        def getSum(root):
            nonlocal summ
            if not root:
                return 0
            
            # if root.val < low or root.val > high:
            #    return 0
            
            if low <= root.val  and root.val <= high:
                summ += root.val
            
            if root.left and low < root.val:
                getSum(root.left)
            
            if root.right and high > root.val:
                getSum(root.right)
        
        getSum(root)
        return summ