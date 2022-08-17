class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        min_prod = nums[0]
        max_prod = nums[0]
        
        global_max = nums[0]
        
        for i in range(1, len(nums)):
            
            temp_max = max_prod
            max_prod = max(nums[i], nums[i]*min_prod, nums[i]*max_prod)
            min_prod = min(nums[i], nums[i]*min_prod, nums[i]*temp_max)
            
            global_max = max(global_max, max_prod)
        
        return global_max
        