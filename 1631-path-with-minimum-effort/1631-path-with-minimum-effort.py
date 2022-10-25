class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        pq = []
        nrows = len(heights)
        ncols = len(heights[0])
        
        diff_mat = [[float('inf') for _ in range(ncols)] for _ in range(nrows)]
        
        diff_mat[0][0] = 0
        
        heapq.heappush(pq, (0, 0, 0))
        
        
        while pq:
            
            val, i, j = heapq.heappop(pq)
            
            for neigh in [(0,1), (1, 0), (0, -1), (-1, 0)]:
                
                x = i+neigh[0]
                y = j+neigh[1]
                
                if x < 0 or x >= nrows or y < 0 or y >= ncols:
                    continue
                
                max_diff = max(val, abs(heights[i][j] - heights[x][y]))
                
                if max_diff < diff_mat[x][y]:
                    diff_mat[x][y] = max_diff
                    heapq.heappush(pq, (max_diff, x, y))
                    
            
        return diff_mat[-1][-1]