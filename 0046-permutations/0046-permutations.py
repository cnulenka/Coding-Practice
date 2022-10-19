class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        res = []
        
        def perm(index):
            nonlocal n, res
            
            if index == n:
                res.append(list(nums))
                return
            
            for i in range(index, n):
                
                nums[i], nums[index] = nums[index], nums[i]
                
                perm(index+1)
                
                nums[index], nums[i] = nums[i], nums[index]
                
                
        perm(0)
        return res
                
                
                