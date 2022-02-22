class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        
        visited = [False for _ in range(len(s))]
        q = collections.deque([0])
        visited[0] = True
        
        while q:
            start = q.popleft()
            #if visited[start]:
            #    continue
            
            
            for end in range(start+1, len(s)+1):
                if s[start:end] in wordDict:
                    #print(start, end)
                    
                    if end == len(s):
                        return True
                    
                    if not visited[end]:
                        q.append(end)
                    
                    visited[end] = True
            
        
        return False