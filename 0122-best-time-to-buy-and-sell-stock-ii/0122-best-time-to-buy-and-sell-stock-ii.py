class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        The key point is we need to consider every peak immediately following a valley to maximize the profit. In case we skip one of the peaks (trying to obtain more profit), we will end up losing the profit over one of the transactions leading to an overall lesser profit.
        '''
        
        n = len(prices)
        dp = {}
        
        def get_profit(ind, buy):
            
            if ind == n:
                return 0
            
            if (ind, buy) in dp:
                return dp[(ind, buy)]
            
            profit = 0
            if buy:
                profit = max(
                    -prices[ind] + get_profit(ind+1, 1-buy),
                    get_profit(ind+1, buy)
                )
            else:
                profit = max(
                    prices[ind] + get_profit(ind+1, 1-buy),
                    get_profit(ind+1, buy)
                )
            
            dp[(ind, buy)] = profit
            return dp[(ind, buy)]
                
        
        return get_profit(0, 1)