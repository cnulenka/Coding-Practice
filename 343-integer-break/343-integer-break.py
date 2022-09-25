class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [None, 1]
        for num in range(2, n+1):
            max_prod = 1
            i = num - 1
            j = 1
            
            while i>=j:
                max_prod = max(max_prod, max(i, dp[i]) * max(j, dp[j]))
                i-=1
                j+=1
            
            dp.append(max_prod)
        return dp[n]
            