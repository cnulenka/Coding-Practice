class Solution {
    public int maxProfit(int[] prices) {

        int res = 0, mini = prices[0];
        int[] profits = new int[prices.length];
        for(int i = 0; i < prices.length; i++){
            mini = Math.min(mini, prices[i]);
            res = Math.max(prices[i] - mini, res);
            profits[i] = res;
        }

        int total_max = 0, maxi = prices[prices.length-1], res2 = 0;
        for(int i = prices.length-1 ; i>=0 ;i--) {
            maxi = Math.max(maxi, prices[i]);
            res2 = Math.max(maxi - prices[i], res2);
            total_max = Math.max(total_max, profits[i]+res2);
        }

        return total_max;
    }
}