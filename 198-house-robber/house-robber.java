class Solution {
    public int rob(int[] nums) {
        int including = nums[0];
        int excluding = 0;
        int maxAmount = nums[0];

        for(int i = 1; i < nums.length; i++){
            int prevIncluding = including;
            including = excluding + nums[i];
            excluding = Math.max(prevIncluding, excluding);
            maxAmount = Math.max(including, excluding);
        }

        return maxAmount;
    }
}