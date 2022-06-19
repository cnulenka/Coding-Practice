class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1] * (amount+1)
        dp[0] = 0
        #print(dp)
        for i in range(1, amount+1):
            for j in range(len(coins)):
                if i-coins[j] >= 0:
                    # print(dp[i], dp[i-coins[j]])
                    dp[i] = min(dp[i], dp[i-coins[j]] + 1)
        
        return -1 if dp[amount] > amount else dp[amount]
                    