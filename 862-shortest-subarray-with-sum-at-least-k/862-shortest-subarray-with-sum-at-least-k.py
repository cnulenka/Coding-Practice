class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        
        pre_sum = [0]
        n = len(nums)
        
        for x in nums:
            pre_sum.append(x + pre_sum[-1])
        
        
        ans = n + 1
        import collections
        mq = collections.deque()
        
        
        for i,pi in enumerate(pre_sum):
            
            while mq and pi <= pre_sum[mq[-1]]:
                mq.pop()
                
            
            while mq and pi - pre_sum[mq[0]] >= k:
                ans = min(ans, i - mq[0])
                mq.popleft()
            
            
            mq.append(i)
                
        return ans if ans<n+1 else -1
        