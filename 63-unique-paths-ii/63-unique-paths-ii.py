class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        nrows = len(obstacleGrid)
        ncols = len(obstacleGrid[0])
        
        if obstacleGrid[nrows - 1][ncols - 1] == 1:
            return 0
        
        for i in range(nrows -1, -1, -1):
            for j in range(ncols -1, -1, -1):
                
                if i == nrows-1 and j == ncols - 1:
                    obstacleGrid[nrows - 1][ncols - 1] = 1
                else:
                    if obstacleGrid[i][j] == 1:
                        obstacleGrid[i][j] = -1
                    else:
                        from_right = 0
                        if j+1 < ncols and obstacleGrid[i][j+1] != -1:
                                from_right = obstacleGrid[i][j+1]
                        
                        from_left = 0
                        if i+1 < nrows and obstacleGrid[i+1][j] != -1:
                                from_left = obstacleGrid[i+1][j]
                        
                        obstacleGrid[i][j] += from_right + from_left
                    #print(obstacleGrid)
        
        
        return obstacleGrid[0][0] if obstacleGrid[0][0] > 0 else 0