class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        res =[]
        n = len(nums)
        
        def permute(index):
            nonlocal res
            if index == n:
                res.append(list(nums))
                return
            
            s = set()
            for i in range(index, n):
                
                # trick use set instead of i,i-1 check
                # as nums r swaped
                if nums[i] in s:
                    continue
                s.add(nums[i])
                nums[i], nums[index] = nums[index], nums[i]
                permute(index+1)
                nums[index], nums[i] =  nums[i], nums[index]                
        
        permute(0)
        return res