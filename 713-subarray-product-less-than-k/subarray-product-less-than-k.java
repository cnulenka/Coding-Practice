class Solution {
    public int numSubarrayProductLessThanK(int[] nums, int k) {
        int left = 0, right = 0, currProduct = 1, count = 0;
        while(right < nums.length){
            
            currProduct *= nums[right];
            while(currProduct >= k && left <= right){
                currProduct = currProduct/nums[left];
                left++;
            } 
            
            // same as other sliding window
            // trick instead of max, just add the length
            // include all subarray in that length
            count += right-left+1;
            right++;
        } 

        return count;
    }
}