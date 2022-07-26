class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        rows = len(grid)
        cols = len(grid[0])
        
        def dfs(i, j):
            if i >= rows or i < 0:
                return 0
            
            if j >= cols or j < 0:
                return 0
            
            if visited[i][j] or grid[i][j] == 0:
                return 0
            
            visited[i][j] = True
            
            left = dfs(i, j-1)
            right = dfs(i, j+1)
            up = dfs(i-1, j)
            down = dfs(i+1, j)
            
            return left + right + up + down + 1
            
        
        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not visited[i][j] and grid[i][j] == 1:
                    area = dfs(i,j)
                    max_area = max(max_area, area)
        
        
        return max_area
        
        
        