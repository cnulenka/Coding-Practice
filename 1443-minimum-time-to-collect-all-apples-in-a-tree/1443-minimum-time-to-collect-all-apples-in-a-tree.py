class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        
        graph = [[] for i in range(n)]
        
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
            
        # print(graph)
            
        visited = [False for i in range(n)]
            
        def dfs(i):
            
            if visited[i]:
                return 0
            
            visited[i] = True
            
            ans = 0
            
            for neigh in graph[i]:
                if not visited[neigh]:
                    ans += dfs(neigh)
                    
            return ans + 2 if (ans or hasApple[i]) else ans
        
        res = dfs(0)
        return res - 2 if res else 0
        
        