class Solution {
    public int minGroups(int[][] intervals) {
    // train platform, meeting rooms
   Arrays.sort(intervals, (a, b) -> a[0] == b[0] ? a[1] - b[1] : a[0] - b[0]);
		Queue<Integer> minHeap = new PriorityQueue<>();
		for (int[] interval: intervals) {
			int left = interval[0];
			int right = interval[1];
			if (!minHeap.isEmpty() && left > minHeap.peek()) {
                // poll in case of over lap
                // sabse chota vala end hi new interval le skta
                // hai, else koi nahi le skta so just increase
                // min heap size i.e add that interval  to list
				minHeap.poll();
			}
            //  always push right to heap
			minHeap.offer(right);
		}
		return minHeap.size();
	}
}