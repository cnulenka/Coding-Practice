# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        prev = -1
        curr_count = 0
        max_count = 0
        res = []
        
        def inorder(root):
            nonlocal prev, curr_count, max_count, res
            
            if not root:
                return
            
            inorder(root.left)
            
            if root.val == prev:
                curr_count+=1
            else:
                curr_count = 1 # also make it one on first occur
            
            if curr_count > 0 and curr_count == max_count:
                res.append(root.val) # trick assign curr node val not prev
            elif curr_count > max_count:
                res = [root.val]
                max_count = curr_count
            
            prev = root.val
            
            inorder(root.right)
        
        
        inorder(root)
        #print(prev, curr_count, max_count, res)
        
        # if curr_count > 0 and curr_count == max_count:
        #     res.append(prev)
        # elif curr_count > max_count:
        #     res = [prev]
        #     max_count = curr_count
                    
        return res
        