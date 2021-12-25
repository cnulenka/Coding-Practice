class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        
        def clean_queue(i):
            
            while deq and deq[0] <= i-k:
                deq.popleft()
                
            while deq and nums[deq[-1]] <= nums[i]:
                deq.pop()
        
        
        deq = deque()
        
        n = len(nums)
        out = []
        
        for i in range(n):
            clean_queue(i)
            deq.append(i)
            if i >= k - 1:
                out.append(nums[deq[0]])
        
        return out