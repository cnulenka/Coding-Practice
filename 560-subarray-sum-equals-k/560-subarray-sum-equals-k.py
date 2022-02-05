class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_map = defaultdict(int)
        curr_sum = 0
        count = 0
        
        for i in range(len(nums)):
            curr_sum += nums[i]
            
            if curr_sum == k:
                count += 1
                
            
            count += sum_map[curr_sum - k]
            
            sum_map[curr_sum] += 1
        
        return count