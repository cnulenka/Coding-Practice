class Solution {
    public int rob(int[] nums) {
        int include = nums[0], maxAmount = nums[0];
        int exclude = 0;

        for(int i = 1 ; i < nums.length ; i++){

            int prevInclude = include;
            include = exclude + nums[i];
            exclude = Math.max(prevInclude, exclude);
            maxAmount = Math.max(include, exclude);
        }

        return maxAmount;
    }
}