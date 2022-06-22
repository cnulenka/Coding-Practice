# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def helper(left, right):
            nonlocal index_map, pre_order_index
            
            if left > right:
                return None
            
            val = preorder[pre_order_index]
            pre_order_index += 1
            index = index_map[val]
            root = TreeNode(val)
            
            root.left = helper(left, index -1)
            root.right = helper(index+1, right)
            
            return root
        
        
        index_map = {}
        pre_order_index = 0
        for index, node in enumerate(inorder):
            index_map[node] = index
        
        return helper(0, len(inorder) - 1)