class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        curr_search_space = 0
        farthest = 0
        
        for i in range(len(nums)-1):
            farthest = max(farthest, i+nums[i])
            
            if i == curr_search_space:
                jumps += 1
                curr_search_space = farthest
        
        return jumps