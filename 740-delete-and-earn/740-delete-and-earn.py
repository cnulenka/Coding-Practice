class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        from collections import Counter
        freq = Counter(nums)
        
        max_num = max(nums)
        arr = [0] * (max_num+1)
        
        for k,v in freq.items():
            arr[k] = k*v
            
        n = len(arr)
        rob_next_plus_one = 0
        rob_next = arr[n-1]
        
        for i in range(n-2, -1, -1):
            curr = max(rob_next, rob_next_plus_one+arr[i])
            
            rob_next_plus_one = rob_next
            rob_next = curr
            
        return rob_next