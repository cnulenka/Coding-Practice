class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # find 3 maximum, max1, max2, max3
        # find 2 min, min1, min2
        
        nums.sort()
        
        return max(nums[-1]*nums[-2]*nums[-3], nums[-1]*nums[0]*nums[1])