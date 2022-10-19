class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        
        visited = [False for _ in range(len(s))]
        q = collections.deque([0])
        
        while q:
            
            start = q.popleft()
            
            if start == len(s):
                return True
            
            # if start > len(s):
            #     continue
            
            # print(start)
            if visited[start]:
                continue
            
            for ind in range(start, len(s)):
                
                if s[start:ind+1] in wordDict:
                    q.append(ind+1)
            
            # explored all possibilities
            visited[start] = True
        

        return False