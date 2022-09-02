class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = defaultdict(list)
        
        for account in accounts:
            for i in range(2, len(account)):
                graph[account[1]].append(account[i])
                graph[account[i]].append(account[1])
        
        visited = set()
        
        def dfs(node, emails):
            
            visited.add(node)
            emails.append(node)
            
            for neigh in graph[node]:
                if neigh not in visited:
                    dfs(neigh, emails)
        
        res = []
        for account in accounts:
            if account[1] not in visited:
                emails = []
                dfs(account[1], emails)
                emails.sort()
                curr_res = [account[0]]
                curr_res.extend(emails)
                res.append(curr_res)
        
        return res
        
        
        
        
            