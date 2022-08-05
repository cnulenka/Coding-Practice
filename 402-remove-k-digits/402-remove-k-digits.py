class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        # tricky test cases, multiple failures
        # 100 1, 9 1, 10200 1, 10, 2
        nums = [ int(char) for char in num]
        
        if len(nums) == k:
            return "0"
        
        stack = []
        for i in range(len(nums)):
            while k and stack and nums[i] < nums[stack[-1]]:
                #print(nums[i], )
                stack.pop()
                k -= 1
            #print(stack, k)
            stack.append(i)
        
        # catch # edge case # only increasing input
        while k:
            stack.pop()
            k -= 1
        
        #print(stack)
        stack = [ str(nums[char]) for char in stack]
        stack = "".join(stack)
        stack = int(stack)
        stack = str(stack)
        return stack