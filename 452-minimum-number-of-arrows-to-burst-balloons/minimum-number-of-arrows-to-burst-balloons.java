class Solution {
    public int findMinArrowShots(int[][] points) {
        if (points.length == 0) return 0;
        // sort on basis of end time in asc
       Arrays.sort(points, (o1, o2) -> {
            // We can't simply use the o1[1] - o2[1] trick, as this will cause an 
            // integer overflow for very large or small values.
            if (o1[1] == o2[1]) return 0;
            if (o1[1] < o2[1]) return -1;
            return 1;
        });
        int arrows = 1;
        int k = 1, n = points.length, end = points[0][1];
        while(k < n) {
            if(points[k][0] > end){
                arrows +=1;
                end = points[k][1];
            }
            k++;
        }   

        return arrows;
    }
}