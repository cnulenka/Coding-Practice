class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0
        r = 0
        n = len(s)
        dp = {}
        max_length = 0
        
        for r in range(n):
            if s[r] in dp and dp[s[r]] >= 0:
                while l <= dp[s[r]]:
                    dp[s[l]] = -1
                    l+=1
                
            max_length = max(max_length, r-l+1)

            dp[s[r]] = r
            
        return max_length