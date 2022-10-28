class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        
        self.__matrix = matrix
        self.__nrows = len(matrix)
        self.__ncols = len(matrix[0])
        
        for i in range(self.__nrows):
            for j in range(self.__ncols):
                
                up, left, diag = 0, 0, 0
                
                if i-1 >= 0:
                    left = self.__matrix[i-1][j]
                    
                if j-1 >= 0:
                    up = self.__matrix[i][j-1]
                    
                if i-1 >= 0 and j-1 >= 0:
                    diag = self.__matrix[i-1][j-1]
                
                
                self.__matrix[i][j] +=  up + left - diag
        
        # print(self.__matrix)
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        up, left, diag = 0, 0, 0
        
        if row1 - 1 >= 0:
            up = self.__matrix[row1-1][col2]
            
        if col1 - 1 >= 0:
            left = self.__matrix[row2][col1-1]
        
        if row1 - 1 >= 0 and col1 - 1 >= 0:
            diag = self.__matrix[row1-1][col1-1]
        
        
        return self.__matrix[row2][col2] - up - left + diag


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)