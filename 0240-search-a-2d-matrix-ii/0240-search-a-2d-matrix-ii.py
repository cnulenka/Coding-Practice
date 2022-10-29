class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        nrows = len(matrix)
        ncols = len(matrix[0])
        
        i = 0
        j = ncols - 1
        
        while i < nrows and j >= 0:
            
            if target == matrix[i][j]:
                return True
            elif target > matrix[i][j]:
                i+=1
            else:
                j-=1
        
        
        return False
            