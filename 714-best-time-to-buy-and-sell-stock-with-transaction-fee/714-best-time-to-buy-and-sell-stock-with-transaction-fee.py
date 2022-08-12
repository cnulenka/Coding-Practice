class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp = {}
        def solve(ind, buy):
            
            if ind >= n:
                return 0
            
            if (ind, buy) in dp:
                return dp[(ind, buy)]
            
            if buy:
                
                profit = max(-prices[ind] + solve(ind+1, not buy), 
                            solve(ind+1, buy))
            else:
                
                profit = max(prices[ind] - fee + solve(ind+1, not buy),
                            solve(ind+1, buy))
            
            dp[(ind, buy)] = profit
            return dp[(ind, buy)]
        
        return solve(0, 1)