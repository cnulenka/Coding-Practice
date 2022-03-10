class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        color = dict()
        
        for node in range(len(graph)):
            if node not in color:
                q = collections.deque([node])
                color[node] = 0
                while q :
                    node = q.popleft()
                    for neig in graph[node]:
                        if neig in color:
                            if color[neig] == color[node]:
                                return False
                        else:
                            color[neig] = 1 - color[node]
                            q.append(neig)
        
        return True
                