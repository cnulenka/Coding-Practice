class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        // sort by increasing end
        Arrays.sort(intervals, (a,b) -> a[1]-b[1]);
        int prev =  0;
        int n = intervals.length;
        int numErase = 0;
        for(int i = 1; i < n ; i++){
            // trick -> greedy --> remove the one with
            // longer end date
            if(intervals[prev][1] > intervals[i][0]){
                // if this happens means intersection
                // and we have to remove either prev or curr
                if(intervals[prev][1] > intervals[i][1]){
                    // if prev one is greater than current one
                    // remove prev one else remove the curr one
                    prev = i;
                }
                numErase += 1;
            } else {
                prev = i;
            }
        }

        return numErase;
    }
}