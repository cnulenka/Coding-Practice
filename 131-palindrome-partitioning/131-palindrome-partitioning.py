class Solution:
    def isPalindrome(s, i, j):
        while i <= j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
    
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def solve(s, i, j, pl):
            #print(pl)
            if i >= j:
                if pl:
                    #print(pl, "hola")
                    res.append(copy.deepcopy(pl))
                    #print(res, "res")
                return;
    
            for k in range(i, j):
                if Solution.isPalindrome(s, i, k):
                    pl.append(s[i:k+1])
                    solve(s, k+1, j, pl)
                    pl.pop()
                    
        
        solve(s, 0, len(s), [])
        return res