class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        nrows = len(matrix)
        ncols = len(matrix[0])
        
        max_size = 0
        
        for i in range(nrows):
            for j in range(ncols):
                
                if int(matrix[i][j]):
                
                    up = left = diag = 0

                    if i-1 >= 0:
                        up = int(matrix[i-1][j])

                    if j-1 >= 0:
                        left = int(matrix[i][j-1])

                    if i-1 >= 0 and j-1 >= 0:
                        diag = int(matrix[i-1][j-1])

                    matrix[i][j] = int(matrix[i][j]) + min(up, left, diag)
                    
                    max_size = max(max_size, matrix[i][j])
            
            
        return max_size**2
                    
                    