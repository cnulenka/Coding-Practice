class Solution {
    public int numIslands(char[][] grid) {
        
        int nrows = grid.length;
        int ncols = grid[0].length;

        int[][] visited = new int[nrows][ncols];

        int numIslands = 0;
        for(int i = 0; i< nrows; i++) {
            for(int j = 0; j<ncols; j++){
                if(grid[i][j] == '1' && visited[i][j] != 1){
                    dfs(i,j,grid, visited);
                    numIslands++;
                }
            }
        }       

        return numIslands;
    }

    private void dfs(int x, int y, char[][] grid, int[][] visited) {

        if(x < 0 || x >= grid.length || y < 0 || y >= grid[0].length){
            // boundary checks
            return;
        }

        if(visited[x][y] == 1) {
            // if already visited
            return;
        }

        if(grid[x][y] == '0') {
            return;
        }

        visited[x][y] = 1;

        int[][] dirs = new int[][] {{0,1}, {1,0}, {-1,0}, {0,-1}};
        for(int[] dir: dirs){
            int newx = dir[0] + x;
            int newy = dir[1] + y;
            dfs(newx, newy, grid, visited);
        }

        return;
    }
}