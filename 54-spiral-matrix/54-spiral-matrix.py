class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        
        def solve(r1, c1, r2, c2):
            
            nonlocal res
            nonlocal matrix
            
            if r1>=r2 or c1>=c2:
                return
            
            for i in range(c1, c2):
                res.append(matrix[r1][i])
                
            for i in range(r1+1, r2):
                res.append(matrix[i][c2-1])
            
            if r2-1 > r1:
                for i in range(c2-2, c1-1, -1):
                    res.append(matrix[r2-1][i])
            
            if c1 < c2-1:
                for i in range(r2-2, r1, -1):
                    res.append(matrix[i][c1])

            
            solve(r1+1, c1+1, r2-1, c2-1)
            
        
        res = []
        solve(0,0,len(matrix), len(matrix[0]))
        
        return res
        