class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        res = []
        comb = []
        
        def solve(index):
            
            if len(comb) == k:
                res.append(list(comb))
                
            for i in range(index, n+1):
                comb.append(i)
                solve(i+1)
                comb.pop()
        
        solve(1)
        return res