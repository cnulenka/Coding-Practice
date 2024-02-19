class Solution {
    public int minPathSum(int[][] grid) {
        int nrows = grid.length;
        int ncols = grid[0].length;
        int[][] dp = new int[nrows][ncols];

        for(int i = nrows - 1; i >= 0; i--){
            for(int j = ncols -1 ; j>=0 ; j--){
                if(i == nrows -1 && j == ncols -1){
                    dp[i][j] = grid[i][j];
                } else {
                    int right = Integer.MAX_VALUE;
                    if(i+1 < nrows){
                        right = dp[i+1][j];
                    }
                    int left = Integer.MAX_VALUE;
                    if(j+1 < ncols){
                        left = dp[i][j+1];
                    }
                    dp[i][j] = grid[i][j] + Math.min(left, right);
                }
            }
        }

        return dp[0][0];
    }
}