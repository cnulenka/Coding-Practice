# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def getInorderSuccessor(self, root):
        
        root = root.right
        while root.left:
            root = root.left
        return root
    
    def getInorderPredecessor(self, root):
        
        root = root.left
        while root.right:
            root = root.right
        return root
    
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        if not root:
            return
        
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left and not root.right:
                root = None
            elif root.right:
                successor = self.getInorderSuccessor(root)
                root.val = successor.val
                root.right = self.deleteNode(root.right, successor.val)
            else:
                pred = self.getInorderPredecessor(root)
                root.val = pred.val
                root.left = self.deleteNode(root.left, pred.val)
        
        return root
                