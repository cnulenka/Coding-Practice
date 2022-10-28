class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        n = len(nums)
        res = []
        
        def solve(index, comb):
            
            res.append(list(comb))
            
            for i in range(index, n):
                
                if i > index and nums[i] == nums[i-1]:
                    continue
                    
                comb.append(nums[i])
                solve(i+1, comb)
                comb.pop()
                
        
        solve(0, [])
        return res
                
                
        