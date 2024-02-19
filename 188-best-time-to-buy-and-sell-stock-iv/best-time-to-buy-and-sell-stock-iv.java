class Solution {

    private int solve(int index, int buy, int limit, int[] prices, int[][][] dp) {

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

        if(limit == 0 || index == prices.length){
            return 0;
        }

        if(dp[index][buy][limit] != -1){
            return dp[index][buy][limit];
        }

        int profit = 0;

        if(buy == 1) {
            profit = Math.max(-prices[index] + solve(index+1, 1-buy, limit, prices, dp) ,
                                solve(index+1, buy, limit, prices, dp));
        } else {
            // only decrease limit in case of sell
            profit = Math.max(prices[index] + solve(index+1, 1-buy, limit - 1, prices, dp) ,
                                solve(index+1, buy, limit, prices, dp));
        }

        dp[index][buy][limit] = profit;
        return profit;
    }

    public int maxProfit(int k, int[] prices) {
        int[][][] dp = new int[prices.length+1][2][k+1];
        for(int i = 0; i < prices.length+1; i++){
            for(int j = 0; j < 2; j++){
                for(int l = 0; l<k+1;l++){
                    dp[i][j][l] = -1;
                }
            }
        }
        return solve(0, 1,k, prices, dp);
    }
}