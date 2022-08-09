class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        The key point is we need to consider every peak immediately following a valley to maximize the profit. In case we skip one of the peaks (trying to obtain more profit), we will end up losing the profit over one of the transactions leading to an overall lesser profit.
        '''
        
        n = len(prices)
        dp = {} # dp[n][2]
        
        def get_max_profit(ind, buy): # buy can be 0 or 1
            
            if ind == n:
                return 0
            
            if (ind, buy) in dp:
                return dp[(ind, buy)]
            
            if buy:
                profit = max(-prices[ind] + get_max_profit(ind+1, not buy), get_max_profit(ind+1, buy))
            else:
                profit = max(prices[ind] + get_max_profit(ind+1, not buy), get_max_profit(ind+1, buy))
            
            dp[(ind, buy)] = profit
            return dp[(ind, buy)]
        
        return get_max_profit(0, 1)