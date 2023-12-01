class Solution {
    public int leastInterval(char[] tasks, int n) {
        PriorityQueue<Integer> pq = new PriorityQueue<>((a,b) -> b-a);
        Queue<int[]> queue = new LinkedList<>();
        Map<Character, Integer> map = new HashMap<>();
        for(char c : tasks){
            map.putIfAbsent(c, 0);
            map.put(c, map.get(c)+1);
        }

        for(Map.Entry<Character, Integer> entry : map.entrySet()){
            pq.offer(entry.getValue());   
        }

        int time = 0;
        // simulate the whole behavior
        while(pq.size() > 0 || queue.size() > 0){
            time += 1;
            //System.out.println("time: "+ time);

            // take out from hq
            // jo highest freq hai usko pehle nikalo
            if(pq.size() > 0) {
                Integer top = pq.poll();
                //System.out.println(top);
                // reduce freq and insert
                top -= 1;
                if (top > 0) {
                    // jab ek type ka nikal liya, next
                    // u can only take out after n mins 
                    queue.offer(new int[]{top, time+n});
                }
            }

            if(queue.size() > 0 && queue.peek()[1] == time) {
                // push back to heap if enough time has passed
                pq.offer(queue.peek()[0]);
                queue.poll();
            }
        }

        return time;
    }
}