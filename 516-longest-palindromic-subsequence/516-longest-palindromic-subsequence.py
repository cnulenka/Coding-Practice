class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        dp = {}
    
        def lcs(a, b, m, n):
            #print(a, b, m, n)
            if (m,n) in dp:
                return dp[(m,n)]
            
            if n == 0 or m == 0:
                dp[(m,n)] = 0
                return 0
            
            if a[m-1] == b[n-1]:
                dp[(m,n)] = 1 + lcs(a,b, m-1,n-1)
                return dp[(m,n)]
            
            dp[(m-1,n)] = lcs(a,b, m-1, n)
            dp[(m,n-1)] = lcs(a,b, m, n-1)
            dp[(m,n)] = max(dp[(m-1,n)] , dp[(m,n-1)])
            return dp[(m,n)]
        
        n = len(s)
        lcs(s, s[::-1], n, n)
        #print(dp)
        return dp[(n,n)]