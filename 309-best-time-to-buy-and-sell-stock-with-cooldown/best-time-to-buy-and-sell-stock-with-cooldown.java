class Solution {

    private int solve(int index, int buy, int[] prices, int[][] dp) {

        /*
        at each step we can either buy or sell
        buy 
            - buy the item # include
            - dont do anything # exlcude
        sell
            - sell the item # include
            - dont do anything # exlcude
            
        sell is only possible after buy
        for index 0 it will always be buy, no sell possible
        */

        if(index >= prices.length){ // should be equal to as +2 is done for sell
            return 0;
        }

        if(dp[index][buy] != -1){
            return dp[index][buy];
        }

        int profit = 0;

        if(buy == 1) {
            profit = Math.max(-prices[index] + solve(index+1, 1-buy, prices, dp) ,
                                solve(index+1, buy, prices, dp));
        } else {
            // only decrease limit in case of sell
            profit = Math.max(prices[index] + solve(index+2, 1-buy, prices, dp) ,
                                solve(index+1, buy, prices, dp));
        }

        dp[index][buy] = profit;
        return profit;
    }

    public int maxProfit(int[] prices) {
        int[][] dp = new int[prices.length+1][2];
        for(int i = 0; i < prices.length+1; i++){
            for(int j = 0; j < 2; j++){
                dp[i][j] = -1;
            }
        }
        return solve(0, 1, prices, dp);
    }
}