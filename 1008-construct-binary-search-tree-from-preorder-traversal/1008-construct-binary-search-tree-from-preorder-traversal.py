# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        root = TreeNode(preorder[0])
        s = [root]
        
        for i in range(1, len(preorder)):
            
            node = s[-1]
            child = TreeNode(preorder[i])
            
            while s and s[-1].val < child.val:
                node = s.pop()
            
            if child.val > node.val:
                node.right = child
            else:
                node.left = child
            
            s.append(child)
    
        return root
            