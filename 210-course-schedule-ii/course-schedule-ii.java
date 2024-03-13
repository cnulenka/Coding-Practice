class Solution {

    private Boolean isCyclic(int node, Map<Integer, 
    List<Integer>> adjList, int[] visited, int[] processed, List<Integer> order) {
        
        visited[node] = 1;

        for(int neighbor: adjList.getOrDefault(node, new ArrayList<>())){
            if(processed[neighbor] == 1){
                continue;
            }

            if(visited[neighbor] == 1 || isCyclic(neighbor, adjList, visited, processed, order)){
                return true;
            }
        }

        visited[node] = 0;
        processed[node] = 1;

        order.add(node);
        return false;
    }

    public int[] findOrder(int numCourses, int[][] prerequisites) {

        Map<Integer, List<Integer>> adjList = new HashMap<>();

        for(int[] edge: prerequisites){
            adjList.putIfAbsent(edge[0], new ArrayList<>());
            adjList.get(edge[0]).add(edge[1]);
        }

        int[] visited = new int[numCourses];
        int[] processed = new int[numCourses];
        List<Integer> topologicalSortedOrder = new ArrayList<>();

        for(int i = 0; i< numCourses; i++){
            if(processed[i] == 0 && isCyclic(i, adjList, visited, processed, topologicalSortedOrder)){
                return new int[0];
            }
        }

        int[] order;
        order = new int[numCourses];
        for (int i = 0; i < numCourses; i++) {
            order[i] = topologicalSortedOrder.get(i);
        }

        return order;
    }
}