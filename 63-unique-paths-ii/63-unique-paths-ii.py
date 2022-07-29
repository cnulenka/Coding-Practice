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
                        obstacleGrid[i][j] = 0
                    else:
                        if j+1 < ncols:
                                obstacleGrid[i][j] += obstacleGrid[i][j+1]
                        
                        if i+1 < nrows:
                                obstacleGrid[i][j] += obstacleGrid[i+1][j]
                    
        return obstacleGrid[0][0]