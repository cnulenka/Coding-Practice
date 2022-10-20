class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        res = []
        arr = [1, 2, 3, 4,5 ,6,7,8,9]
        l = len(arr)
        
        def solve(index, comb_sum, comb):
            nonlocal res
            
            if comb_sum == n and len(comb) == k:
                res.append(list(comb))
                
            if comb_sum > n or len(comb) > k:
                return
            
            for i in range(index, l):
                
                comb.append(arr[i])
                comb_sum += arr[i]
                solve(i+1, comb_sum, comb)
                comb_sum -= arr[i]
                comb.pop()
                
        
        solve(0, 0, [])
        return res