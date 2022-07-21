class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        from collections import Counter
        freq = Counter(nums)
        
        max_num = max(nums)
        arr = [0] * (max_num+1)
        
        for k,v in freq.items():
            arr[k] = k*v
            
        max_gain = 0
        excl = 0
        incl = arr[0]
        
        for i in range(1, len(arr)):
            temp = incl
            incl = excl+arr[i]
            excl = max(temp, excl)
            
            max_gain = max(max_gain, max(excl, incl))
            
        return max_gain