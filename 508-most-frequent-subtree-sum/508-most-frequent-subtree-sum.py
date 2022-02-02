# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        
        from collections import defaultdict
        freq_map = defaultdict(int)
        
        def computeSum(root):
            
            nonlocal freq_map
            
            if not root:
                return 0
            
            left_sum = computeSum(root.left)
            right_sum = computeSum(root.right)
            
            
            curr_sum = root.val + left_sum + right_sum
            
            freq_map[curr_sum] += 1
            
            return curr_sum
        
        computeSum(root)
        #print(freq_map)
        max_sum = max(list(freq_map.values()))
        
        res = []
        
        for k,v in freq_map.items():
            if v == max_sum:
                res.append(k)
                
        return res