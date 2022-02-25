class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        
        if m == 0:
            return 0
        
        n = len(obstacleGrid[0])
        
        
        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1]:
            return 0
        
        dp = [[0 for _ in range(n)] for _ in range(m)]
        
        dp[m-1][n-1] = 1
        
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                
                if obstacleGrid[i][j] == 1 or dp[i][j] > 0:
                    continue
                
                if i+1 < m and dp[i+1][j] > 0:
                    dp[i][j] += dp[i+1][j]
                
                if j+1 < n and dp[i][j+1] > 0:
                    dp[i][j] += dp[i][j+1]
        
                #print(dp[i][j], i , j)
        return dp[0][0]