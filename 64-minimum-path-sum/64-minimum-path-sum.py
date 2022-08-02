class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1 , -1):
                if i == m-1 and j == n - 1:
                    continue
                
                left = float('inf')
                right = float('inf')
                
                if i + 1 < m:
                    left = grid[i+1][j]
                
                if j + 1 < n:
                    right  = grid[i][j+1]
                    
                grid[i][j] += min(left, right)
        
        
        return grid[0][0]