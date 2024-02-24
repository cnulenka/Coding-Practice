class Solution {
    public boolean search(int[] nums, int target) {
        int l = 0, r = nums.length - 1, n = nums.length;
        
        while(l <= r) {
            int mid = l + (r-l)/2;
            System.out.println(l + " l " + mid + " mid " + r  + " r");
            
            if(nums[mid] ==  target)
                return true;
            else if((nums[l] == nums[mid]) && (nums[r] == nums[mid]))
            {
                l++;
                r--;
            } else if(nums[mid] >= nums[l] && nums[mid] >= nums[r]) { // which sorted array u r part of left or right
            // you part of left sorted array
                System.out.println(l + " l " + mid + " mid " + r  + " r top");
                if(target < nums[mid] && target >= nums[l]){ // mind the equal to
                     r = mid - 1;
                } else {
                  l = mid+1;
                }
            } else { // which sorted array u r part of left or right
                System.out.println(l + " l " + mid + " mid " + r  + " r bottom");
                if(target > nums[mid] && target <= nums[r]){ // mind the equal to
                     l = mid+1;
                } else {
                     r = mid - 1;
                }
            }
        }

        return false;
    }
}