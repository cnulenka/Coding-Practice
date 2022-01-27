# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        
        dict_map = {}
        delimeter = '$'
        
        
        def map_subtrees(root):
            
            nonlocal dict_map
            nonlocal delimeter
            
            if root is None:
                return delimeter
            
            
            left_hash = map_subtrees(root.left)
            
            
            right_hash = map_subtrees(root.right)
            
            #print(delimeter, str(root.val), left_hash, right_hash)
            hash_str = delimeter + str(root.val) + left_hash + right_hash
            
            if hash_str in dict_map:
                dict_map[hash_str][0] += 1
            else:
                dict_map[hash_str] = [1, root]
                
            
            return hash_str
        
        
        map_subtrees(root)
        dup_hash = []
        for k,v in dict_map.items():
            if v[0] > 1:
                dup_hash.append(v[1])
        #import re
        #for i,v in enumerate(dup_hash):
        #    dup_hash[i] = dup_hash[i].strip('$')
        #    dup_hash[i] = list(map(int, re.split(r'\$+', dup_hash[i])))
        
        return dup_hash