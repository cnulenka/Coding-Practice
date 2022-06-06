class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        
        @functools.lru_cache(maxsize=None)
        def dfs(word):
            nonlocal dic
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]
                
                if prefix in dic and suffix in dic:
                    return True
                if prefix in dic and dfs(suffix):
                    return True
                if suffix in dic and dfs(prefix):
                    return True
            
            return False
        
        res = []
        dic = set(words)
        for word in words:
            if dfs(word):
                res.append(word)
        
        return res