class Solution {
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, (a,b) -> a[0]-b[0]);
        LinkedList<int[]> merged = new LinkedList<>();
        merged.add(intervals[0]);
        for(int i = 0; i< intervals.length;i++){
            if(merged.getLast()[1]  >= intervals[i][0]){
                merged.getLast()[1] = Math.max(merged.getLast()[1], intervals[i][1]);
            } else  {
                merged.add(intervals[i]);
            }
        }

        return merged.toArray(new int[merged.size()][]);
    }
}