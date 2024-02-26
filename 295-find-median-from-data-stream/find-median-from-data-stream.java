class MedianFinder {
    Queue<Integer> minHeap;
    Queue<Integer> maxHeap;
    public MedianFinder() {
        minHeap = new PriorityQueue<>();
        maxHeap = new PriorityQueue<>((a,b) -> b-a);
    }
    
    public void addNum(int num) {
        // insert in min heap always
        minHeap.offer(num);

        // you now need to balance, what if a smaller number 
        // is in min heap
        maxHeap.offer(minHeap.poll());

        // always keep one more in maxHeap
        if(minHeap.size() + 1 < maxHeap.size()){
            minHeap.offer(maxHeap.poll());
        }
    }
    
    public double findMedian() {
        if(minHeap.size() == maxHeap.size()){
            double sum = minHeap.peek() + maxHeap.peek();
            return sum/2;
        }
        return maxHeap.peek();
    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder obj = new MedianFinder();
 * obj.addNum(num);
 * double param_2 = obj.findMedian();
 */