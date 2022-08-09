class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = {}
        
        '''
        at each step we can either buy or sell
        buy 
            - buy the item
            - dont do anything
        sell
            - sell the item
            - dont do anything
            
        sell is only possible after buy
        for index 0 it will always be buy, no sell possible
        '''
        
        def solve(ind, buy, cap):
            
            if cap == 0 or ind == n:
                return 0
            
            if (ind, buy, cap) in dp:
                return dp[(ind, buy, cap)]
            
            if buy:
                profit = max(-prices[ind] + solve(ind+1, not buy, cap), solve(ind+1, buy, cap))
            else:
                profit = max(prices[ind] + solve(ind+1, not buy, cap - 1), solve(ind+1, buy, cap))
            
            dp[(ind, buy, cap)] = profit
            return dp[(ind, buy, cap)]
        
        return solve(0, 1, 2)
                
        
          