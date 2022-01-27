# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        from collections import defaultdict
        dict_map = defaultdict(int)
        delimeter = '$'
        dup_hash = []
        
        
        def map_subtrees(root):
            
            nonlocal dict_map, delimeter, dup_hash
            
            if root is None:
                return delimeter
            
            
            left_hash = map_subtrees(root.left)
            
            
            right_hash = map_subtrees(root.right)
            
            hash_str = delimeter + str(root.val) + left_hash + right_hash
            
            dict_map[hash_str] += 1
            if dict_map[hash_str] == 2:
                dup_hash.append(root)
                
            
            return hash_str
        
        
        map_subtrees(root)
        
        return dup_hash