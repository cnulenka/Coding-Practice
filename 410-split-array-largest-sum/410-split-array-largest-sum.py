class Solution:
    def numSplits(self, target_sum, nums):
        curr_sum = 0
        splits = 0
        
        for num in nums:
            curr_sum += num
            
            if curr_sum > target_sum:
                splits += 1
                curr_sum = num
        
        return splits + 1
        
    def splitArray(self, nums: List[int], m: int) -> int:
        
        left = max(nums)
        right = sum(nums)
        res = []
        
        while left <= right:
            
            max_sum = (left + right)//2
            
            splits = self.numSplits(max_sum, nums)
            
            if splits > m:
                left = max_sum + 1
            else:
                right = max_sum - 1
                res = max_sum
        
        
        return res
                