class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        l = 0
        r = n-1
        
        res = 0
        mod = 10**9 + 7
        
        while l <= r :
            if nums[l] + nums[r] <= target:
                res += pow(2, r-l, mod)
                l += 1
            else:
                r -= 1
            
        return res%mod