class Solution:
    def trap(self, height: List[int]) -> int:
        
        n = len(height)
        
        left = 0
        right = n-1
        
        left_max = height[0]
        right_max = height[n-1]
        
        water = 0
        
        while left <= right:
            # process the smaller height first
            # if height[left] > height[right]:
            if left_max > right_max:
                # process right
                right_max = max(right_max, height[right])
                water += right_max - height[right]
                right -= 1
            else:
                # process left
                left_max = max(left_max, height[left])
                water += left_max - height[left]
                left += 1
                
        
        return water
            