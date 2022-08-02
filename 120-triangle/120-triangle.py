class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        nrows = len(triangle)
        for i in range(nrows - 2, -1 , -1):
            ncol = len(triangle[i])
            for j in range(ncol):
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
        
        return triangle[0][0]