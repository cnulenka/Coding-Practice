class Solution:
    def rob(self, nums: List[int]) -> int:
        incl, excl = nums[0], 0
        
        maxi = nums[0]
        
        for i in range(1, len(nums)):
            
            temp = incl
            incl = excl + nums[i]
            excl = max(temp, excl)
            
            maxi = max(maxi, max(excl,incl))
        
        
        return maxi
            
            