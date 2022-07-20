class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = {}
        def solve(i, coin_sum):
            
            if (i, coin_sum) in dp:
                return dp[(i, coin_sum)]
            
            if coin_sum == amount:
                return 1
            
            if coin_sum > amount or i == n:
                return 0
            
            incl = solve(i, coin_sum + coins[i])
            excl = solve(i + 1, coin_sum)
            
            dp[(i, coin_sum)] = incl + excl
            
            return dp[(i, coin_sum)]
    
        return solve(0, 0)