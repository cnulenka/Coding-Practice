# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        # populate parent pointers
        
        def dfs(root):
            
            if not root:
                return
            
            if root.left:
                root.left.par = root
                dfs(root.left)
                
            if root.right:
                root.right.par = root
                dfs(root.right)
        
        root.par = None
        dfs(root)
        
        q = collections.deque([(target, 0)])
        seen = {target}
        
        while q:
            if q[0][1] == k:
                return [node.val for node, _ in q]
            node, dis = q.popleft()
            for nei in [node.left, node.right, node.par]:
                if nei and nei not in seen:
                    seen.add(nei)
                    q.append((nei, dis+1))
        
        return []
        
        