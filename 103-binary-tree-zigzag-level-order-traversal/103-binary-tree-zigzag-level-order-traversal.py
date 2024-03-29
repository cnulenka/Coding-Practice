# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        
        res = []
        
        def bfs(root):
            q = deque([root])
            level = 1
            while q:
                n = len(q)
                temp_res = deque()
                for i in range(n):
                    front = q.popleft()
                    if level%2 == 0:
                        temp_res.appendleft(front.val)
                    else:
                        temp_res.append(front.val)
                    if front.left:
                        q.append(front.left)
                    if front.right:
                        q.append(front.right)
                        
                res.append(temp_res)
                level += 1
        
        bfs(root)
        return res
                        
                
                