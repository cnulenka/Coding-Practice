class Solution:
    
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        p_count = [0 for _ in range(26)]
        s_count = [0 for _ in range(26)]
        
        for c in p:
            p_count[ord(c) - ord('a')] += 1
            
        res = []
        l = 0    
        for r in range(len(s)):
            # print(l,r)
            s_count[ord(s[r]) - ord('a')] += 1
            
            if s_count == p_count:
                res.append(l)
            
            if r-l+1 == len(p):
                s_count[ord(s[l]) - ord('a')] -= 1
                l += 1
        
        return res