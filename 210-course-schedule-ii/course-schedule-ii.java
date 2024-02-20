class Solution {

  Map<Integer, List<Integer>> adjList;
  int[] visited;
  int[] processed;
  List<Integer> topologicalOrder;

  private boolean isCyclic(int node) {

      if(visited[node] == 1){
          return true;
      }

      visited[node] = 1;

      for(int neigh: adjList.getOrDefault(node, new ArrayList<>())){
          if(processed[neigh] == 1){
              continue;
          }

            if(isCyclic(neigh)){
                return true;
            }
      }

    visited[node] = 0;
    processed[node] = 1;
    topologicalOrder.add(node);
    return false;
  }

  public int[] findOrder(int numCourses, int[][] prerequisites) {

    adjList = new HashMap<>();
    visited = new int[numCourses];
    processed = new int[numCourses];
    topologicalOrder = new ArrayList<>();

    // Create the adjacency list representation of the graph
    for (int i = 0; i < prerequisites.length; i++) {
      int dest = prerequisites[i][0];
      int src = prerequisites[i][1];
      List<Integer> lst = adjList.getOrDefault(src, new ArrayList<Integer>());
      lst.add(dest);
      adjList.put(src, lst);
    }

    // If the node is unprocessed, then call dfs on it.
    for (int i = 0; i < numCourses; i++) {
      if (processed[i] == 0) {
            if(isCyclic(i)){
                return new int[0];
            }
      }
    }

    int[] order;
    order = new int[numCourses];
    for (int i = 0; i < numCourses; i++) {
    order[i] = topologicalOrder.get(numCourses - i - 1);
    }

    return order;
  }
}