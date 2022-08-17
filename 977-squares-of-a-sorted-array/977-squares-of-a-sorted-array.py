class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = 0
        n = len(nums)
        r = n - 1
        
        res = [0 for _ in range(n)]
        i = n - 1
        
        while l <= r:
            #print(nums[l],nums[r])
            if abs(nums[r]) > abs(nums[l]):
                res[i] = nums[r]**2
                r -= 1
            else:
                res[i] = nums[l]**2
                l += 1
            
            i -= 1
        
        return res
                