class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        visited = [ False for _ in range(len(s))]
        q = collections.deque([(0, "")])
        
        res = []
        
        while q:
            
            start, word = q.popleft()
            
            if start == len(s):
                #print(word_list)
                res.append(word)
                continue
            
            # if visited[start]:
            #     continue
            
            curr_str = ""
            root_word = word
            for ind in range(start, len(s)):
                
                curr_str += s[ind]
                
                if curr_str in wordDict:
                    
                    if word:
                        word += " "
                        
                    word += curr_str
                    # print(word)
                    q.append((ind+1, word))
                    
                    word = root_word
            
            visited[start] = True
        
        return res