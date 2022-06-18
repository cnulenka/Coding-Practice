class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = {}
        def solve(i, curr_sum):
            nonlocal n
            if i == n:
                if curr_sum == target:
                    return 1
                return 0
            
            if (i, curr_sum) in dp:
                return dp[(i,curr_sum)]
            
            add = solve(i+1, curr_sum+nums[i])
            sub = solve(i+1, curr_sum-nums[i])
            
            dp[(i,curr_sum)] = add + sub
            
            return dp[(i,curr_sum)]
        
        return solve(0, 0)
            