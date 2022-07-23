class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        
        n = len(s)
        sr = s[::-1]
        # print(s, sr)
        dp = [[-1 for _ in range(n+1)] for _ in range(n+1) ]
        # print(dp)
        for i in range(n+1):
            dp[i][0] = 0
            dp[0][i] = 0
        # print(dp)
        for i in range(1, n+1): #s
            for j in range(1, n+1): #sr
                if s[i-1] == sr[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        
        # print(dp)
        return dp[n][n]