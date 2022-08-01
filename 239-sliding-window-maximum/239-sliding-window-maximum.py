class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        n = len(nums)
        q = deque()
        
        for i in range(n):
            #print(q, i, k)
            while q:
                if q[0] + k - 1 < i:
                    q.popleft()
                else:
                    break
            #print(q, i, k, "mid")
            if not q:
                q.append(i)
            else:
                while q:
                    if nums[i] >= nums[q[-1]]:
                        q.pop()
                    else:
                        break
                q.append(i)
            #print(q, i, k, "end")
            if i >= k - 1:
                res.append(nums[q[0]])
        
        # [1, -1]
        # 1
        
        return res
        
        
        