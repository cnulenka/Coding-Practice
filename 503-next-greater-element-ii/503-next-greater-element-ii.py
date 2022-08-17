class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        stack = []
        n = len(nums)
        res = [-1 for _ in range(n)]
        
        for i in range(2*n):
            
            k = i%n
            while stack and nums[stack[-1]] < nums[k]:
                top = stack.pop()
                res[top] = nums[k]
            
            stack.append(k)
        
        return res
                    