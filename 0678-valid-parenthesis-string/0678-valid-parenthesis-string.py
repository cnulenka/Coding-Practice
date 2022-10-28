class Solution:
    def checkValidString(self, s: str) -> bool:
        
        # tricky solution
        # must do again
        
        lo = hi = 0 # lowest and highest possible open brackets
        
        for c in s:
            
            lo += 1 if c == "(" else -1
            hi += 1 if c !=")" else -1
            
            # at any point
            # number of highest open brackets
            # is -ve
            if hi < 0:
                return False
            
            lo = max(lo, 0)
            
        # lowest possible opne brackets shoule be 0
        return lo == 0