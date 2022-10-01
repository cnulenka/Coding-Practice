class Solution:
    
    def matchExtendFromCorners(self, l, r, s):
        n = len(s)
         
        while l >= 0 and r < n and s[l] == s[r]:
            l -=1
            r +=1

        # get the correct indexes
        l += 1
        r -= 1

        return r - l + 1, l , r
    
    def longestPalindrome(self, s: str) -> str:
        
        if not s or len(s) < 1:
            return ""
        
        max_len = 1
        start = 0
        end = 0
        
        for i in range(len(s) - 1):
            # don't generate the string everytime
            # rather update only indexes

            max_len_temp, s_temp, e_temp = self.matchExtendFromCorners(i, i, s)
            if max_len_temp > max_len:
                max_len = max_len_temp
                start = s_temp
                end = e_temp
            
            if s[i] == s[i+1]:
                max_len_temp, s_temp, e_temp = self.matchExtendFromCorners(i, i+1, s)
                if max_len_temp > max_len:
                    max_len = max_len_temp
                    start = s_temp
                    end = e_temp
        
        return s[start:end+1]