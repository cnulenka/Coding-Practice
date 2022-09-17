class Solution:
    def jump(self, nums: List[int]) -> int:
        
        # trick start from 0
        # dont initialise to first element
        # loop till n-1 elements
        max_reach = 0
        curr_reach = 0
        jump = 0
        
        for i in range(len(nums)-1):
            max_reach = max(max_reach, nums[i]+i)
            if curr_reach == i:
                jump += 1
                curr_reach = max_reach
        
        return jump
            
            
        