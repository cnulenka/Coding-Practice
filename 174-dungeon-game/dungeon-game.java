class Solution {

    private int minHealthForNext(int x, int y, int nrows, int ncols,
            int[][] minCost, int currCellCost) {

        if (x >= nrows || x < 0 || y >= ncols || y < 0) {
            return Integer.MAX_VALUE;
        }

        return Math.max(1, minCost[x][y] - currCellCost);

    }

    public int calculateMinimumHP(int[][] dungeon) {
        int nrows = dungeon.length;
        int ncols = dungeon[0].length;
        int[][] minCost = new int[nrows][ncols];

        for (int i = 0; i < nrows; i++) {
            Arrays.fill(minCost[i], Integer.MAX_VALUE);
        }

        for(int i = nrows - 1; i >= 0 ; i--) {
            for(int j = ncols -1 ; j>=0 ; j--){

                int right = minHealthForNext(i, j+1, nrows, ncols, minCost, dungeon[i][j]);
                int down = minHealthForNext(i+1, j, nrows, ncols, minCost, dungeon[i][j]);
                int minHealthForNext = Math.min(right, down);

                if(minHealthForNext != Integer.MAX_VALUE){
                    minCost[i][j] = minHealthForNext;
                } else {
                    minCost[i][j] = dungeon[i][j] >= 0 ? 1 : 1 - dungeon[i][j];
                }
            }
        }

        return minCost[0][0];
    }
}