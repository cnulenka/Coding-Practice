class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        l = 0
        r = 0
        n = len(nums)
        num_zero = 0
        res = 0
        
        while r < n:
            
            if nums[r] == 0:
                num_zero += 1
                
            while num_zero > k:
                if nums[l] == 0:
                    num_zero -= 1
                    
                l += 1
            res = max(res, r-l+1)
            r += 1
            
        return res
        
        