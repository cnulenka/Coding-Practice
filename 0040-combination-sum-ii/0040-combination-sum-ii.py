class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        n = len(candidates)
        candidates.sort()
        
        def solve(index, comb_sum, comb):
            
            if comb_sum == target:
                res.append(list(comb))
                
            if comb_sum > target:
                return
                
            for i in range(index, n):
                
                # trick
                # compare i with i-1
                # as they are sorted
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                
                comb.append(candidates[i])
                comb_sum += candidates[i]
                solve(i+1, comb_sum, comb)
                comb.pop()
                comb_sum -= candidates[i]
                
        solve(0, 0, [])
        return res