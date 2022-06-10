class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_max_arr = [0] * n
        right_max_arr = [0] * n
        
        left_max = -1
        for i in range(n):
            left_max = max(left_max, height[i])
            left_max_arr[i] = left_max
        
        
        right_max = -1
        for i in range(n - 1, -1, -1):
            right_max = max(right_max, height[i])
            right_max_arr[i] = right_max
        
        res = 0
        for i in range(n):
            w = min(left_max_arr[i], right_max_arr[i]) - height[i]
            res += w if w > 0 else 0
        
        return res