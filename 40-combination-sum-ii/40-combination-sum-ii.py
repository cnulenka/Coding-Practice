class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        
        def backtrack(comb, remain, start):
            # print(comb, remain , start)
            
            if remain == 0:
                results.append(list(comb))
                return
            
            if remain < 0:
                return
            
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                
                # sorted hence this optimazation can be done. CATCH
                # if remain - candidates[i] < 0:
                #     break
                comb.append(candidates[i])
                
                backtrack(comb, remain - candidates[i], i+1)
                
                comb.pop()
        
        candidates.sort()
        backtrack([], target, 0)
        return results