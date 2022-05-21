class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        open_seen, balance = 0,0
        res1 = []
        
        for c in s:
            if c == '(':
                open_seen +=1
                balance +=1
            elif c == ')':
                if balance == 0:
                    continue
                balance -= 1
            res1.append(c)
        
        res = []
        valid_open = open_seen - balance
        for c in res1:
            if c == '(':
                if valid_open == 0:
                    continue
                else:
                    valid_open -= 1 
            res.append(c)
        
        return res
                