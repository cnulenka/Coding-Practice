class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        n = len(candidates)
        def solve(index, comb, comb_sum):
            nonlocal res
            
            if comb_sum == target:
                res.append(list(comb))
                return
            
            if comb_sum > target:
                return
            
            for i in range(index, n):
                comb.append(candidates[i])
                comb_sum += candidates[i]
                solve(i, comb, comb_sum)
                comb.pop()
                comb_sum -= candidates[i]
                
        solve(0, [], 0)
        return res