class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        def solve(row, col):
            nonlocal dic
            if (row, col) in dic:
                return dic[(row,col)]
            path = triangle[row][col]
            if row < len(triangle) - 1:
                dic[(row,col)] = path + min(solve(row+1, col), solve(row+1,col+1))
                return dic[(row,col)]
            return path
        
        dic = {}
        return solve(0,0)