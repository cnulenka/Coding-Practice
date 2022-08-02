class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)
        def max_rob(house):
            #print(house)
            rob_next = house[-1]
            rob_next_of_next = 0
            
            
            for i in range(len(house) - 2, -1, -1):
                
                rob_curr = max(house[i] + rob_next_of_next, rob_next)
                
                rob_next_of_next = rob_next
                rob_next = rob_curr
            
            #print(rob_next)
            return rob_next
        
        # take care of single or no input
        # important for interviews
        if not nums:
            return 0
        
        if n == 1:
            return nums[0]
        
        return max(max_rob(nums[0:n-1]), max_rob(nums[1:n]))