class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last_occur = {c:i for i,c in enumerate(s)}
        seen = set()
        stack = []
        
        for i,c in enumerate(s):
            if c not in seen:
                
                while len(stack) and c < stack[-1] and last_occur[stack[-1]] > i:
                    top = stack.pop()
                    seen.remove(top)
                    
                stack.append(c)
                seen.add(c)
                    
        return "".join(stack)