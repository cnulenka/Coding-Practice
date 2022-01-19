class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        results = []
        
        def backtrack(comb, remain, start):
            
            if remain == 0:
                results.append(list(comb))
            
            if remain < 0:
                return
            
            
            for i in range(start, len(candidates)):
                comb.append(candidates[i])
                
                backtrack(comb, remain - candidates[i], i)
                
                comb.pop()
        
        
        backtrack([], target, 0)
        
        
        return results