class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        res = []
        comb = []
        def solve(index):
            #print(index, comb)
            
            if len(comb) == k:
                res.append(list(comb))
                return
            
            if index > n:
                return
            
            comb.append(index)
            solve(index+1) # include
            comb.pop()
            solve(index+1) # exclude 
        
        solve(1)
        return res