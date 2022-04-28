class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        nrow = len(matrix)
        ncol = len(matrix[0])
        
        dp = [[0 for _ in range(ncol)] for _ in range(nrow)]
        
        total_squares = 0
        
        for i in range(nrow):
            dp[i][0] = matrix[i][0]
            total_squares += dp[i][0]
            
        for i in range(1, ncol):
            dp[0][i] = matrix[0][i]
            total_squares += dp[0][i]
            
        for i in range(1, nrow):
            for j in range(1, ncol):
                if matrix[i][j]:
                    dp[i][j] = min(dp[i-1][j],min(dp[i-1][j-1], dp[i][j-1])) + 1
                    total_squares += dp[i][j]
        
        
        return total_squares
            