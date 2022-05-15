class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        def subarraysWithLessThanKDistinct(nums, k):
            if k == 0:
                return 0
            
            num_subarrays = 0
            diff = 0
            n = len(nums)
            l = 0
            freq = collections.defaultdict(int)
            
            for r in range(n):
                if freq[nums[r]] == 0:
                    diff += 1
                    freq[nums[r]] = 1
                else:
                    freq[nums[r]] += 1
                
                if diff <= k:
                    num_subarrays += r-l+1
                else:
                    while l<n and l<=r and diff>k:
                        freq[nums[l]] -= 1
                        if freq[nums[l]] == 0:
                            diff -= 1
                        l += 1
                    num_subarrays += r-l+1
            #print(num_subarrays)
            return num_subarrays
            
        return subarraysWithLessThanKDistinct(nums, k) - subarraysWithLessThanKDistinct(nums, k-1) 
                        
            