class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        maxi = prices[n-1]
        max_profit = 0
        for i in range(n-2, -1, -1):
            max_profit = max(max_profit, maxi - prices[i])
            maxi = max(prices[i], maxi)
            
        return max_profit
        