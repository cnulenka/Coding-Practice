class Solution:
    def longestConsecutive(self, nums):
        s = set(nums)
        res = 0
        
        for num in s:
            curr_streak = 1
            if num - 1 not in s:
                
                while num + 1 in s:
                    curr_streak += 1
                    num = num + 1 
                
                res = max(curr_streak, res)
        
        
        return res
        
        