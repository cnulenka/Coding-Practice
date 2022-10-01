class Solution:
    
    def matchExtendFromCorners(self, l, r, s):
        n = len(s)
        # print(l,r, "compare")
        
        if s[l] == s[r]:
            
            while l >= 0 and r < n and s[l] == s[r]:
                l -=1
                r +=1
            
            # get the correct indexes
            l += 1
            r -= 1
            
            return r - l + 1, l , r
            
        
        # print(l,r, "result")
        return 0 , l , r
        
    
    def longestPalindrome(self, s: str) -> str:
        
        if not s or len(s) < 1:
            return ""
        
        max_len = 1
        start = 0
        end = 0
        
        for i in range(len(s) - 1):
            # print(start, end, max_len)
            max_len_temp, s_temp, e_temp = self.matchExtendFromCorners(i, i, s)
            if max_len_temp > max_len:
                max_len = max_len_temp
                start = s_temp
                end = e_temp
            
            # print(start, end, max_len)
            max_len_temp, s_temp, e_temp = self.matchExtendFromCorners(i, i+1, s)
            if max_len_temp > max_len:
                max_len = max_len_temp
                start = s_temp
                end = e_temp
        
        return s[start:end+1]