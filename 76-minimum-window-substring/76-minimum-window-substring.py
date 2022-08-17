class Solution:
    
    def compare(self, s_counter, t_counter):
        
        for k,v in t_counter.items():
            if s_counter[k] < v:
                return False
        
        return True
    
    def minWindow(self, s: str, t: str) -> str:
        min_length = float('inf')
        min_str = ""
        
        l = 0
        r = 0
        
        t_counter = defaultdict(int)
        s_counter = defaultdict(int)
        
        for c in t:
            t_counter[c] += 1
        
        while r < len(s):
            s_counter[s[r]] += 1
            
            #print(s_counter)
            #print(t_counter)
            #print("**************************")
            
            while l<=r and self.compare(s_counter, t_counter):
                if r-l+1 < min_length:
                    min_length = r-l+1
                    min_str = s[l:r+1]
                    
                s_counter[s[l]] -= 1
                l += 1
            
            r += 1
        
        return min_str