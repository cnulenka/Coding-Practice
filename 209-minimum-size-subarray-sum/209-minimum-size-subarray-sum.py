class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        curr_sum = 0
        l = 0
        r = 0
        
        min_length = float('inf')
        
        while r < len(nums):
            curr_sum  += nums[r]
            
            #print(l,r,curr_sum)
            
            # move left pointer
            while curr_sum >= target:
                min_length = min(min_length, r-l+1)
                curr_sum -= nums[l]
                l += 1
            
            r += 1
        
        return min_length if min_length!= float('inf') else 0