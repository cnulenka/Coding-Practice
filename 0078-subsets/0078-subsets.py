class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        n = len(nums)
        
        def solve(index, comb):
            
            if index == n:
                res.append(list(comb))
                return
            
            comb.append(nums[index])
            solve(index+1, comb)
            comb.pop()
            solve(index+1, comb)
        
        solve(0,[])
        return res