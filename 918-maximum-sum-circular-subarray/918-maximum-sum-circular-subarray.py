class Solution:
    
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        min_straight_sum = float('inf')
        max_straight_sum = float('-inf')
        array_sum = 0
        temp_min_sum = 0
        temp_max_sum = 0
        
        for i in range(len(nums)):
            array_sum += nums[i]
            temp_min_sum = min(temp_min_sum+nums[i], nums[i])
            min_straight_sum = min(min_straight_sum, temp_min_sum)
            
            temp_max_sum = max(temp_max_sum+nums[i], nums[i])
            max_straight_sum = max(max_straight_sum, temp_max_sum)
            # print(temp_max_sum, max_straight_sum)
        
        #print(min_straight_sum, array_sum, max_straight_sum)
        
        if array_sum == min_straight_sum:
            # if all negative
            return max_straight_sum
        
        return max(max_straight_sum, array_sum-min_straight_sum)
        