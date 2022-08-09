class Solution:
    def countSquares(self, m: List[List[int]]) -> int:
        
        nrows = len(m)
        ncols = len(m[0])
        res = 0
        for i in range(nrows):
            for j in range(ncols):
                if i == 0 or j == 0:
                        pass
                elif m[i][j] == 1:
                    m[i][j] += min(m[i][j-1], m[i-1][j], m[i-1][j-1])
                
                res += m[i][j]
        
        return res