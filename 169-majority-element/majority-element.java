class Solution {
    public int majorityElement(int[] nums) {
        int candidate = nums[0];
        // trick count should be 0
        int count = 0;
        for(int num: nums){
            if(num == candidate){
                count +=1;
            } else {
                if(count == 0){
                    candidate = num;
                    count = 1;
                } else {
                    count -=1;
                }
            }
        }

        return candidate;
    }
}