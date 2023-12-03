class Solution {
    public int change(int amount, int[] coins) {
          int [] dp = new int[amount+1];
          dp[0] = 1;

        // if you first loop is for amount instead of coins, 
        // it wont work, as it counts duplicate

        // Opposite of minimum coins
        // also notice coins is in desceding order

        // to avoid duplicacy, traverse coin in a order, first build
        // with 5, then 5,2 , then 5,2,1 to avoid 1+2, 2+1 duplicacy
          // for(int j = coins.length - 1; j >= 0; j--) { 
        for(int j = 0; j < coins.length; j++) { 
              for(int i = 0; i <= amount; i++) {
                  if(i - coins[j] >= 0){
                      dp[i] += dp[i - coins[j]];
                  }
              }
          }

          return dp[amount];
    }
}