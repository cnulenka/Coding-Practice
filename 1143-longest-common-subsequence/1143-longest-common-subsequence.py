class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        def solve(m, n):
            nonlocal hash_dict
            #print(hash_dict)
            
            if (m,n) in hash_dict:
                return hash_dict[(m,n)]
            
            if m == 0 or n == 0:
                hash_dict[(m, n)] = 0
                return 0
            
            if text1[m-1] == text2[n-1]:
                return 1 + solve(m-1, n-1)
            
            res1 = solve(m-1, n)
            hash_dict[(m-1, n)] = res1
            
            res2 = solve(m, n-1)
            hash_dict[(m, n-1)] = res2
            
            return max(res1, res2)
        
        hash_dict = {}
        return solve(len(text1), len(text2))