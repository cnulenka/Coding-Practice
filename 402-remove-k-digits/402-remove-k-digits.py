class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        # tricky test cases, multiple failures
        # 100 1, 9 1, 10200 1, 10 2
        
        stack = []
        for digit in num:
            while k and stack and digit < stack[-1]:
                #print(nums[i], )
                stack.pop()
                k -= 1
            #print(stack, k)
            stack.append(digit)
        
        # catch # edge case # only increasing input
        while k:
            stack.pop()
            k -= 1
        
        return "".join(stack).lstrip('0') or "0"