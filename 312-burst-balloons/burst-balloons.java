class Solution {
    public int maxCoins(int[] nums) {
        // add 1 before and after nums
        int n = nums.length + 2;
        int[] newNums = new int[n];
        System.arraycopy(nums, 0, newNums, 1, n - 2);
        newNums[0] = 1;
        newNums[n - 1] = 1;

        // cache the results of dp
        int[][] memo = new int[n][n];
        //Bruteforce: Generate all permutations for the ordering of balloons 
        //and check which permutation yields the best profit. But it will take O(n!) time.
        // we can not burst the first one and the last one
        // since they are both fake balloons added by ourselves
        // N^3 time complexity
        return dp(memo, newNums, 1, n - 2);
    }

    public int dp(int[][] memo, int[] nums, int left, int right) {
        if(left > right){
            return 0;
        }

        if(memo[left][right] > 0 ){
            return memo[left][right];
        }

        int max = 0;
        for(int i = left; i <=right ; i++){
            int remaining = dp(memo, nums, left, i-1) + dp(memo, nums, i+1, right);

            // we choose the last one to burst
            // As balloon right + 1 will become adjacent to k after bursting  i + 1 to right balloons
            // As balloon left- 1 will become adjacent to k after bursting  left  to i -1 balloons
            int gain = nums[left - 1] * nums[i] * nums[right + 1];
            max = Math.max(max, gain + remaining);
        }

        memo[left][right]= max;
        return max;
    }
}