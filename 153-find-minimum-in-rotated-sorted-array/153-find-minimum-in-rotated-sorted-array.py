class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        
        if nums[0] < nums[-1]:
            return nums[0]
        
        # take care of end conditions b4 hand
        # if nums[-1] < nums[-2]:
        #     return nums[-1]
        
        # look at your cpp solution
        
        l = 0
        r = len(nums) - 1
        
        while(l <= r):
            mid = l + (r - l)//2
            # print(l, mid, r)
            if (mid == 0 or nums[mid-1] > nums[mid]) and (mid == len(nums) -1 or nums[mid] < nums[mid+1]):
                return nums[mid]
            
            # trick, only focus on two numbers
            # order is important in java
#             if nums[mid] > nums[mid + 1]:
#                 return nums[mid + 1]
            
#             if nums[mid - 1] > nums[mid]:
#                 return nums[mid]
        
        
            # if nums[mid] > nums[0]: # what if mid is 0 itself
            if nums[mid] >= nums[0] and nums[mid] >= nums[-1]:
                l = mid+1
            else:
                r = r - 1
        
        return -1