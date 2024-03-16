class Solution {
    public int longestOnes(int[] nums, int k) {
        int l = 0, r = 0, numZero = 0, maxLen = 0;

        while(r < nums.length){

            if(nums[r] == 0) {
                numZero++;
            }

            while(numZero > k){
                if(nums[l] == 0){
                    numZero--;
                }
                l++;
            }

            maxLen = Math.max(maxLen, r-l+1);
            r++;
        }

        return maxLen;
    }
}