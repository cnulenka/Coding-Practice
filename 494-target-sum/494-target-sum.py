class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = {}
        def solve(i, curr_sum):
            #print(i, curr_sum)
            nonlocal target_sum
            
            if curr_sum > target_sum:
                return 0
            
            if i == n:
                if curr_sum == target_sum:
                    return 1
                else:
                    return 0
            
            if (i,curr_sum) in dp:
                return dp[(i,curr_sum)]
                
            incl = solve(i+1, curr_sum + nums[i])
            excl = solve(i+1, curr_sum)
            
            dp[(i,curr_sum)] = incl + excl
            
            return dp[(i,curr_sum)]
        
        ts = sum(nums)
        if (ts+target) %2 !=0:
            return 0
        target_sum = (ts+target)//2
        #print(target_sum)
        #print(dp)
        return solve(0, 0)
            