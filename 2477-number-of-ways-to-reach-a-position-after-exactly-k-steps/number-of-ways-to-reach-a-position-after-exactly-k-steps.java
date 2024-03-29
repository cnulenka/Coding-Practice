class Solution {
    int mod = 1000000007;
    
    int util(int s, int e, int curr, int k, int[][] dp){
        if(k == 0){
            if(curr == e) return 1;
            return 0;
        }
        if(dp[curr+1001][k] != -1){
            return dp[curr+1001][k];
        }
        
        int a = util(s, e, curr+1, k-1, dp)%mod;
        int b = util(s, e, curr-1, k-1, dp)%mod;
        
        return dp[curr+1001][k] = (a+b)%mod;
        
    }
    
    public int numberOfWays(int s, int e, int k) {
        int[][] dp = new int[3002][1001];
        for(int[] item : dp){
            Arrays.fill(item, -1);
        }
        return util(s, e, s, k, dp);
    }
}