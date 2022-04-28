class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        nrow = len(matrix)
        ncol = len(matrix[0])
        
        dp = [[0 for _ in range(ncol)] for _ in range(nrow)]
        
        total_squares = 0
            
        for i in range(nrow):
            for j in range(ncol):
                if matrix[i][j]:
                    if i == 0 or j == 0:
                        dp[i][j] = matrix[i][j]
                    else:
                        dp[i][j] = min(dp[i-1][j],min(dp[i-1][j-1], dp[i][j-1])) + 1
                    total_squares += dp[i][j]
        
        
        return total_squares
            