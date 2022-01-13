# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class NodeVal:
    
    def __init__(self, maxn = float(-inf), minn = float(inf), maxs = 0, bsum = 0):
        self.max_node = maxn
        self.min_node = minn
        self.max_sum = maxs
        self.sum = bsum

class Solution:
    
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        res = [0]
        def check(node):
            if not node: return 0, True, -inf, inf
            
            s1, bst1, maxi1, mini1 = check(node.left)
            s2, bst2, maxi2, mini2 = check(node.right)
            if bst1 and bst2 and maxi1 < node.val < mini2:
                v = node.val + s1 + s2
                res[0] = max(res[0], v)
                return v, True, max(maxi2, node.val), min(node.val, mini1)
            
            return 0, False, -inf, inf
        
        check(root)
        return res[0]