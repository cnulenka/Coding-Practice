class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        summ = 0
        # put a rem 0 case 
        # tricky
        dp = {0:-1}
        
        for i,n in enumerate(nums):
            
            # summ modulo k
            summ = (summ + n) % k
                
            if summ not in dp:
                dp[summ] = i
            else:
                if i - dp[summ] >= 2:
                    return True
        
        
        return False
            
            
            
            
            
        
        