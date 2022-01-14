# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        
        self.stack = []
        self._left_most_node(root)
    
    def _left_most_node(self, root):
        
        while(root):
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        
        node = self.stack.pop()
        
        self._left_most_node(node.right)
        
        return node.val
        

    def hasNext(self) -> bool:
        
        return len(self.stack)
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()