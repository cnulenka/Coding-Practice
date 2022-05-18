class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        
        addtional = 0
        max_addtional= 0
        n = len(customers)
        
        res = 0
        
        for i in range(n):
            if grumpy[i] == 0:
                res += customers[i]
            else:
                addtional += customers[i]
            
            if i >= minutes:
                addtional -= customers[i-minutes]*grumpy[i-minutes]
            
            max_addtional = max(addtional, max_addtional)
            
        return res + max_addtional