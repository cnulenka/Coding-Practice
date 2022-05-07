class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        graph = [[] for _ in range(26)]
        eqn_with_not = []
        
        for eqn in equations:
            if eqn[1] == '=':
                x = ord(eqn[0]) - ord('a')
                y = ord(eqn[-1]) - ord('a')
                graph[x].append(y)
                graph[y].append(x)
            else:
                eqn_with_not.append(eqn)
        
        color = [None] * 26
        # connected component number
        cc_num = 0
        
        for start in range(26):
            if color[start] is None:
                stack = [start]
                cc_num += 1
                while stack:
                    top = stack.pop()
                    color[top] = cc_num
                    for neigh in graph[top]:
                        if color[neigh] is None:
                            color[neigh] = cc_num
                            stack.append(neigh)
        
        
        for eqn in eqn_with_not:
            x = ord(eqn[0]) - ord('a')
            y = ord(eqn[-1]) - ord('a')
            if color[x] == color[y]:
                return False
        
        return True
        
        
        