class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        low = 0 # catch low points to first 1, initialise with 0th index
        n = len(nums)
        high = n - 1
        i = 0
        while(i <= high):
            if nums[i] == 0:
                nums[i] = 1
                nums[low] = 0
                low += 1
                i += 1
            elif nums[i] == 1:
                i += 1
            elif nums[i] == 2:
                nums[i] = nums[high]
                nums[high] = 2
                high -= 1
        
        return nums
                
        
                
            