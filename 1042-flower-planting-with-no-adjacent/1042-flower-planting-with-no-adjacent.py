class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        
        graph = [[] for _ in range(n)]
        res_color = [0 for _ in range(n)]
        
        for path in paths:
            graph[path[0]-1].append(path[1]-1)
            graph[path[1]-1].append(path[0]-1)
            
        for i in range(n):
            
            colors = [0 for _ in range(5)]
            
            for neig in graph[i]:
                colors[res_color[neig]] = -1
                
            for c in range(1,5):
                if colors[c] != -1:
                    res_color[i] = c
                    break
        
        return res_color
                
            