class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        res = []
        stack = []
        
        for c in s:
            if c == "(":
                res.append(c)
                stack.append(c)
            elif c == ')':
                if stack and stack[-1] == "(":
                    res.append(c)
                    stack.pop()
            else:
                res.append(c)
        
        res2 = deque()
        n = len(res)
        
        for i in range(n -1, -1, -1):
                if stack and res[i] == stack[-1]:
                    stack.pop()
                    continue
                else:
                    res2.appendleft(res[i])
        
        return list(res2)
            
            
        