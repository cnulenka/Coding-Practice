#User function Template for python3

class Solution:
    
    def solve(self, m, n, i, j, path):
        
        #if len(path) > 2:
        #    return
        
        moves = [(0, 1, 'R'), (0, -1, 'L'), (1, 0, 'D'), (-1, 0, 'U')]
        #print(i,j)
        
        if i >= self.rows or i < 0 or j >= self.cols or j < 0:
            return
        
        if m[i][j] == 0 or self.visited[i][j]:
            return
        
        if i == self.rows - 1 and j == self.cols - 1:
            self.res.append("".join(path))
        
        self.visited[i][j] = True
        
        for move in moves:
            path.append(move[2])
            self.solve(m, n, i + move[0], j + move[1], path)
            path.pop()
        
        self.visited[i][j] = False
        
    
    def findPath(self, m, n):
        
        if len(m) == 0 or len(m[0]) == 0 or m[0][0] == 0:
            return []
            
        self.rows = len(m)
        self.cols = len(m[0])
        self.res = []
        self.visited = [[False for _ in m[0]] for _ in m]
        #print(self.visited)
        
        self.solve(m, n, 0, 0, [])
        
        return self.res

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        
        matrix = [[0 for i in range(n[0])]for j in range(n[0])]
        k=0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[k]
                k+=1
        ob = Solution()
        result = ob.findPath(matrix, n[0])
        result.sort()
        if len(result) == 0 :
            print(-1)
        else:
            for x in result:
                print(x,end = " ")
            print()
# } Driver Code Ends