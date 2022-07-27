class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        def solve(curr_index, curr_sum, combination):
            
            if curr_sum == target:
                #print(combination)
                #print(curr_sum)
                res.append(copy.deepcopy(combination))
                return
                
            if curr_sum > target:
                return
            
            if curr_index < 0:
                return
            
            solve(curr_index - 1, curr_sum, combination) # exclude
            combination.append(candidates[curr_index])
            solve(curr_index, curr_sum + candidates[curr_index], combination) # include
            combination.pop()
        
        solve(len(candidates) - 1, 0, list())
        return res