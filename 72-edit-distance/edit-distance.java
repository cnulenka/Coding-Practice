class Solution {
    private int solve(int m, int n, String word1, String word2, int [][]dp){
        if(m == 0 || n == 0){
            return Math.max(m,n);
        }

        if(dp[m][n] != -1){
            return dp[m][n];
        }

        if(word1.charAt(m-1) == word2.charAt(n-1)){
            dp[m][n] = solve(m-1, n-1, word1, word2, dp);
        } else {
            dp[m][n] = 1 + Math.min(
                solve(m-1, n, word1, word2, dp), 
            Math.min(
                solve(m, n-1, word1, word2, dp), 
                solve(m-1,n-1, word1, word2, dp)));
        }

        return dp[m][n];
    }

    public int minDistance(String word1, String word2) {
        int[][] dp = new int[word1.length()+1][word2.length()+1];
        for(int i =0; i<word1.length()+1;i++){
            Arrays.fill(dp[i], -1);
        }
        return solve(word1.length(), word2.length(), word1, word2, dp);
    }
}