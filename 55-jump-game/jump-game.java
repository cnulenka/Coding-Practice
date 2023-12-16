class Solution {
    public boolean canJump(int[] nums) {
        int currReach = nums[0];
        // for(int i = nums.length - 2 ; i >= 0 ; i--) {
        //     // could i have reached des from i
        //     // the i is new destination
        //     if (i+nums[i] >= des){
        //         des = i;
        //     }
        // }

        for(int i = 1; i< nums.length; i++) {
            if(currReach < i) {
                return false;
            }
            currReach = Math.max(i+nums[i], currReach);
        }

        return currReach >= nums.length-1;
    }
}