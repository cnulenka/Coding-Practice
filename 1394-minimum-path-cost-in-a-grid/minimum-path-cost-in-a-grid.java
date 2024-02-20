class Solution {
    public int minPathCost(int[][] nums, int[][] mo) {
        int n = nums.length;
      int m = nums[0].length;
        int[][] dp = new int[n+1][m+1];
        for(int i=0;i<m;i++)dp[n-1][i] = nums[n-1][i];
        for(int i=n-2;i>=0;i--)
        {
            for(int j=0;j<m;j++)
            {
                int ans=Integer.MAX_VALUE;
                for(int k=0;k<m;k++)
                {
                    ans = Math.min(ans, dp[i+1][k]+ mo[nums[i][j]][k]);
                }
                dp[i][j] = ans+nums[i][j];
            }
        }
         int ans=Integer.MAX_VALUE;
        for(int i=0;i<m;i++)
        {
           ans = Math.min(ans,dp[0][i]); 
        }
        return ans;
    }
}