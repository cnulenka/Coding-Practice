class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        candidate = nums[0]
        count = 0
        
        for num in nums:
            if num != candidate:
                if count:
                    count -= 1
                else:
                    candidate = num
            else:
                count += 1
                
        
        return candidate
        