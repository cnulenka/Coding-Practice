class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        if n == 1:
            return nums
        
        i = n - 1
        
        max_index = n-1
        max_num = nums[n-1]
        
        while i-1 >= 0 and nums[i] <= nums[i-1]: 
            i -= 1
            
        if i == 0:
            # fully decreasing order
            return nums.sort()
        
        # print(i, max_index)
        j = i
        while j < n and nums[j] > nums[i-1]: 
            j+=1
        
        nums[i-1], nums[j-1] = nums[j-1], nums[i-1]
        
        
        nums[i:] = sorted(nums[i:])
        
        return nums