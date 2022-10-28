class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        n = len(nums)
        
        def solve(index, comb):
    
            res.append(list(comb))
        
            if index == n:
                    return
            
            for i in range(index, n):
                comb.append(nums[i])
                solve(i+1, comb)
                comb.pop()
        
        solve(0,[])
        return res