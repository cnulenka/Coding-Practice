class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        dp_dict = {}
        def solve(nums, target_sum, index):
            
            if (target_sum, index) in dp_dict:
                return dp_dict[(target_sum, index)]
            
            if target_sum == 0:
                # if target_sum is 0, empty subset is always possible
                dp_dict[(target_sum, index)] = True
                return dp_dict[(target_sum, index)]
            
            if index == 0:
                # if no items in array, no sum is possible except 0
                dp_dict[(target_sum, index)] = False
                return dp_dict[(target_sum, index)]
            
            if target_sum >= nums[index]:
                dp_dict[(target_sum, index)] = solve(nums, target_sum - nums[index], index - 1) or solve(nums, target_sum, index - 1)
            else:
                dp_dict[(target_sum, index)] = solve(nums, target_sum, index - 1)
            return dp_dict[(target_sum, index)]
            
        
        
        array_sum = sum(nums)
        half_sum = array_sum // 2
        
        #print(half_sum, array_sum)
        if half_sum * 2 != array_sum:
            return False
        
        return solve(nums, half_sum, len(nums) - 1)