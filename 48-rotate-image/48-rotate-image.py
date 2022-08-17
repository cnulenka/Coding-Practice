class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        # transpose
        nrows = len(matrix)
        ncols = len(matrix[0])
        
        for i in range(nrows):
            for j in range(ncols):
                if i > j:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                    
        #print(matrix)
        for j in range(ncols//2):
            for i in range(nrows):
                #print(i,j)
                matrix[i][j], matrix[i][ncols - j - 1] = matrix[i][ncols - j - 1], matrix[i][j]
                
        
        return matrix            