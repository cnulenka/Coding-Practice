class Solution {
    public boolean possibleBipartition(int n, int[][] dislikes) {
        // build graph
        Map<Integer, Set<Integer>> graph = new HashMap<>();
        for(int[] edge: dislikes){
            graph.putIfAbsent(edge[0], new HashSet<>());
            graph.putIfAbsent(edge[1], new HashSet<>());
            graph.get(edge[0]).add(edge[1]);
            graph.get(edge[1]).add(edge[0]);
        }

        int[] color = new int[n+1];
        Arrays.fill(color, -1);

        for(int i = 1; i<=n ; i++)
        {
            if(color[i] != -1){
                continue;
            }
            Queue<Integer> queue = new LinkedList<>();
            queue.offer(i);
            color[i] = 0;

            while(!queue.isEmpty()) {
                Integer node = queue.poll();
                for(int neigh : graph.getOrDefault(node, new HashSet<>())){
                    if(color[neigh] != -1){
                        if(color[neigh] == color[node]) {
                            return false;
                        }
                    } else {
                        color[neigh] = 1-color[node];
                        queue.offer(neigh);
                    }
                }
            }
        }
        

        return true;
    }
}