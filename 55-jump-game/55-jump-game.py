class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        des = n-1
        for i in range(n-2, -1, -1):
            if i+nums[i] >= des:
                des = i
        
        return des == 0
            
        