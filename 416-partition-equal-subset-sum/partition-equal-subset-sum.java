class Solution {

    int[][] dp;

    private boolean solve(int[] nums, int ind, int targetSum) {

        if(targetSum == 0) {
            return true;
        }

        if(ind == nums.length || targetSum < 0) {
            return false;
        }

        if(dp[ind][targetSum] != -1){
            return dp[ind][targetSum] == 1;
        }

        // include
        boolean include = solve(nums, ind + 1, targetSum - nums[ind]);
        // exclude
        boolean exclude = solve(nums, ind+1, targetSum);

        if(include || exclude){
            dp[ind][targetSum] = 1;
        } else {
            dp[ind][targetSum] = 0;
        }
        
        return dp[ind][targetSum] == 1;
    }

    public boolean canPartition(int[] nums) {
        int sum = 0;
        for(int num : nums){
            sum+=num;
        }

        if(sum%2 != 0) {
            return false;
        }

        int targetSum = sum/2;
        dp = new int[nums.length][targetSum+1];
        for(int i = 0 ; i < nums.length ; i++) {
            Arrays.fill(dp[i], -1);
        }

        return solve(nums, 0, targetSum);
    }
}