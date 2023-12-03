class Solution {

    Boolean[][] memo;

    private boolean subSetSum(int targetSum, int currIndex, int[] nums){

        if(nums.length == currIndex ||  targetSum < 0) {
            return false;
        }

        if(targetSum == 0){
            return true;
        }

        if (memo[targetSum][currIndex] != null)
            return memo[targetSum][currIndex];

        boolean include = subSetSum(targetSum - nums[currIndex], currIndex+1, nums);
        boolean exclude = subSetSum(targetSum, currIndex+1, nums);

        boolean res =  include || exclude;
        memo[targetSum][currIndex] = res;
        return res;
    }

    public boolean canPartition(int[] nums) {
        int sum = 0;
        for(int n: nums){
            sum+=n;
        }

        if(sum%2 != 0){
            return false;
        }

        int targetSum = sum/2,  n = nums.length;
        memo = new Boolean[targetSum + 1][n + 1];
        return subSetSum(targetSum, 0, nums);
    }
}