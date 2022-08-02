class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        nrows = len(matrix)
        ncols = len(matrix[0])
        # for row in matrix:
        #     print(row)
        
        for i in range(nrows-2, -1, -1):
            for j in range(ncols):
                mini = float('inf')   
                for neigh in [[1, -1], [1, 0], [1, 1]]:
                    if 0 <= j + neigh[1]  and j + neigh[1] < ncols:
                        # print(i,j)
                        # print(matrix[i + neigh[0]][j + neigh[1]], neigh, i + neigh[0], j + neigh[1])
                        # print("------------------")
                        mini = min(mini, matrix[i + neigh[0]][j + neigh[1]])
                
                matrix[i][j] += mini
        # print()
        # for row in matrix:
        #     print(row)
        return min(matrix[0])
                    