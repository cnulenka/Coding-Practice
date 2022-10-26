class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        def compare_dict(s_counter, t_counter):
            
            for k,v in t_counter.items():
                if s_counter[k] < v:
                    return False
                
            return True
        
        
        t_counter = Counter(t)
        s_counter = defaultdict(int)
        
        l = 0
        r = 0
        n = len(s)
        res = n+1
        st = 0
        e = -1
        
        
        while r < n:
            
            s_counter[s[r]] += 1
            
            while l<=r and compare_dict(s_counter, t_counter):
                #print(l,r, res)
                
                if r-l+1 < res:
                    st = l
                    e = r
                    res = r-l+1
                
                #print(st, e)
                s_counter[s[l]] -= 1
                l += 1
            r+=1
        #print(st,e)
        return s[st:e+1]
            
            