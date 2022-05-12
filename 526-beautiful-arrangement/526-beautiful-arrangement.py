class Solution:
    def countArrangement(self, n: int) -> int:
        visited = [False] * (n+1)
        count = 0
        
        def calculate(pos):
            nonlocal count
            nonlocal visited
            
            if pos > n:
                count += 1
                return
            
            for i in range(1, n+1):
                if not visited[i] and (pos%i == 0 or i%pos == 0): 
                    visited[i]=True
                    calculate(pos+1)
                    visited[i]=False
        
        calculate(1)
        return count