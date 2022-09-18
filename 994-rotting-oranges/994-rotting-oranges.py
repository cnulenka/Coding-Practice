class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        num_rotten = 0
        
        nrows = len(grid)
        ncols = len(grid[0])
        fresh_oranges = 0
        
        for i in range(nrows):
            for j in range(ncols):
                if grid[i][j] == 2:
                    q.append((i,j, 0))
                    num_rotten += 1
                elif grid[i][j] == 1:
                    fresh_oranges += 1
        max_min = 0
        
        while q:
            
            i, j, mini = q.popleft()
            max_min = max(max_min, mini)
            
            for _dir in [(i+1,j), (i-1,j), (i, j+1), (i, j-1)]:
                
                if _dir[0] >= 0 and _dir[0] < nrows and _dir[1] >=0 and _dir[1] < ncols:
                    if grid[_dir[0]][_dir[1]] == 0:
                        continue
                    elif grid[_dir[0]][_dir[1]] == 1:
                        grid[_dir[0]][_dir[1]] = 2
                        q.append((_dir[0], _dir[1], mini+1))
                        fresh_oranges -= 1
        
        return max_min if not fresh_oranges else -1