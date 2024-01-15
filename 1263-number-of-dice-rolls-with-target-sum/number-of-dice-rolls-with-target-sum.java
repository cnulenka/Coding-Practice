class Solution {
    int mod = 1000000007;
    int dp[][];

    private int solve(int n, int k, int target){
        if (target == 0 && n == 0){
            return 1;
        }

        if(target < 0 || n < 0){
            return 0;
        }

        if(dp[n][target] !=-1){
            return dp[n][target];
        }

        int numWays = 0;
        for(int i = 1; i <= k ; i++) {
            numWays += solve(n-1, k, target - i) % mod;
            numWays = numWays % mod;
        }

        dp[n][target] = numWays;
        return numWays;
    }

    public int numRollsToTarget(int n, int k, int target) {
        dp = new int[n+1][target+1];
        for(int i = 0; i < n+1; i++){
            Arrays.fill(dp[i], -1);
        }
        solve(n,k,target);
        return dp[n][target];
    }
}