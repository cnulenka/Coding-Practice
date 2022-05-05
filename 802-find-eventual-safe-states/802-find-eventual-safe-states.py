class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        safe = [False] * n
        
        graph = [set(neighbors) for neighbors in graph]
        #print(graph)
        rgraph = [set() for _ in graph]
        
        q = collections.deque()
        
        for i, nodes in enumerate(graph):
            if not nodes:
                q.append(i)
            else:
                for node in nodes:
                    rgraph[node].add(i)
                
        #print(q)
        while q:
            node = q.popleft()
            #print(node)
            safe[node] = True
            for neigh in rgraph[node]:
                graph[neigh].remove(node)
                if len(graph[neigh]) == 0:
                    q.append(neigh)
        
        return [i for i, is_safe in enumerate(safe) if is_safe]