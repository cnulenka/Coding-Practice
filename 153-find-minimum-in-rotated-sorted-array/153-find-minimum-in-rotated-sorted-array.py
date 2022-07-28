class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        
        if nums[0] < nums[-1]:
            return nums[0]
        
        if nums[-1] < nums[-2]:
            return nums[-1]
        
        l = 0
        r = len(nums) - 1
        
        while(l <= r):
            mid = l + (r - l)//2
            # print(l, mid, r)
            if nums[mid-1] > nums[mid] and nums[mid] < nums[mid+1]:
                return nums[mid]
            else:
                if nums[mid] > nums[0]:
                    l = mid+1
                else:
                    r = r - 1
        
        return -1