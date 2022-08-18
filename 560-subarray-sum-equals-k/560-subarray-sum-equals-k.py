class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        dp = defaultdict(int)
        count = 0
        curr_sum = 0
        
        for i in range(len(nums)):
            
            curr_sum += nums[i]
            
            if curr_sum == k:
                count += 1
            
            # trick, no else
            count += dp[curr_sum - k]
                
            dp[curr_sum] += 1
                
        return count