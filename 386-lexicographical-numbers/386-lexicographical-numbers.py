class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        
        def dfs(curr, n):
            nonlocal res
            if curr > n:
                return
            else:
                res.append(curr)
                for i in range(10):
                    temp = 10*curr+i
                    if temp > n:
                        return
                    dfs(temp, n)
        
        res = []
        for i in range(1,10):
            dfs(i,n)
        
        return res