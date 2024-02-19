class Solution {
    public int maxProfit(int[] prices) {
        int res = 0, mini = prices[0];
        for(int i = 1; i < prices.length; i++){
            mini = Math.min(mini, prices[i]);
            res = Math.max(prices[i] - mini, res);
        }

        return res;
    }
}