class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        n = len(nums)
        q = deque()
        
        for i in range(n):
            #print(q, i, k)
            while q and q[0] <= i - k:
                    q.popleft()

            if not q:
                q.append(i)
            else:
                while q and nums[i] >= nums[q[-1]]:
                        q.pop()
                q.append(i)
            #print(q, i, k, "end")
            if i >= k - 1:
                res.append(nums[q[0]])
        
        # [1, -1]
        # 1
        
        return res
        
        
        