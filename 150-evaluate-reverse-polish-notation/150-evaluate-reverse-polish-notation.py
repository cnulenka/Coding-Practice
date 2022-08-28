class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        n = len(tokens)
        i = 0
        
        while i < n:
            
            if tokens[i] not in ['+', '*', '-', '/']:
                stack.append(tokens[i])
            else:
                right = stack.pop()
                left = stack.pop()
                res = eval(left + tokens[i] + right)
                stack.append(str(int(res)))
            
            i += 1
        
        return stack[0]
            
    
            