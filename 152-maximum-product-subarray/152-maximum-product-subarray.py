class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        min_so_far = nums[0]
        max_so_far = nums[0]
        max_product = max_so_far
        
        for i in range(1, len(nums)):
            
            
            temp_max = max(nums[i], min_so_far*nums[i], max_so_far*nums[i])
            min_so_far = min(nums[i], min_so_far*nums[i], max_so_far*nums[i])
            
            max_product = max(max_product, temp_max)
            max_so_far = temp_max
        
        
        return max_product