class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        dp = {}
        nrows = len(matrix)
        ncols = len(matrix[0])
        
        def dfs(i, j):
            
            if (i, j) in dp:
                return dp[(i,j)]
            
            max_length = 0
            
            for d in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                x = i+d[0]
                y = j+d[1]
                if  0 <= x < nrows and 0 <= y < ncols and matrix[x][y] > matrix[i][j]:
                    length = dfs(x, y)
                    dp[(x,y)] = length
                    max_length = max(max_length, length)
                
            return max_length + 1
        
        max_length = 0
        for i in range(nrows):
            for j in range(ncols):
                if (i,j) not in dp:
                    length = dfs(i, j)
                    dp[(i,j)] = length
                    max_length = max(max_length, length)
        
        return max_length
        