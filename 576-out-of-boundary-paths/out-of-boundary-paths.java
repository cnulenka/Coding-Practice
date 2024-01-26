class Solution {

    // Bruteforce = Time complexity : O(4^n), n is maxMove
    // O(mnN). We need to fill the memo array once with dimensions m×n×N times

    static int mod = 1000000007;
    int[][][] dp;

    private int dfs(int m, int n, int maxMove, int i, int j) {

        if( i < 0 || i == m || j < 0 || j == n) {
            //dp[i][j][maxMove]=1; will cause out of bound
            // no need coz u will assign this value in parent
            return 1;
        }

        if(maxMove == 0) {
            return 0;
        }

        //System.out.println(dp[i][j][maxMove]);
        if(dp[i][j][maxMove] >= 0){
            return dp[i][j][maxMove];
        }

        int numWays = 0;
        int[][] dirs = {{0,1}, {1,0}, {-1,0}, {0,-1}}; 
        for(int[] dir: dirs) {
            numWays += dfs(m,n,maxMove - 1, i+dir[0], j+dir[1]) % mod;
            numWays = numWays%mod; // missing this led to WA
        }

        dp[i][j][maxMove] = numWays;
        return dp[i][j][maxMove];
    }

    public int findPaths(int m, int n, int maxMove, int startRow, int startColumn) {
        dp = new int[m][n][maxMove+1];
        for(int i = 0; i < m ; i++){
            for(int j = 0; j<n; j++){
                for(int k = 0; k<maxMove+1; k++){
                    dp[i][j][k] = -1;
                }
            }
        }
        //System.out.println(dp[0][0][0]);
        return dfs(m,n,maxMove, startRow, startColumn)%mod;
    }
}