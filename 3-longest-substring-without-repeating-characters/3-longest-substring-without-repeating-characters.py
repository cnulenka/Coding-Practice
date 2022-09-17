class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0
        r = 0
        n = len(s)
        dp = {}
        res = 0
        
        for r in range(n):
            # print(dp)
            if s[r] in dp and dp[s[r]] >= 0:
                while l <= dp[s[r]]:
                    dp[s[l]] = -1
                    l+=1
                
            res = max(res, r-l+1)
            # print(l, r, res)
            dp[s[r]] = r
            
        return res