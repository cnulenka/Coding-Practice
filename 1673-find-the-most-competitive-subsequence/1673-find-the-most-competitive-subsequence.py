class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        st = []
        
        if len(nums) == 1:
            return nums
        
        st.append(nums[0])
        
        
        i = 1
        
        while i < len(nums):
            
            while len(st) and st[-1] > nums[i] and len(nums) - i > k - len(st):
                st.pop()
                
            
            if len(st) < k:
                st.append(nums[i])
            
            i += 1
        
        return st