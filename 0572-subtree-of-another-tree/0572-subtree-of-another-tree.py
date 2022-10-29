# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        tree_str = ""
        
        def serialize(node):
            
            nonlocal tree_str
            
            if not node:
                # print(tree_str)
                tree_str += "#"
                # print(tree_str)
                return
            
            tree_str += f"^{node.val}"
            serialize(node.left)
            serialize(node.right)
            
            
        serialize(root)
        root_str = tree_str

        tree_str = ""
        serialize(subRoot)
        subroot_str = tree_str
        
        # print(root_str)
        # print(subroot_str)
        
        return subroot_str in root_str