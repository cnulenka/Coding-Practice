class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        sum_map = dict()
        sum_map[0] = -1
        
        summ = 0
        res = 0
        for i, num in enumerate(nums):
            
            summ+= 1 if num == 1 else -1
            
            if summ in sum_map:
                res = max(res, i - sum_map[summ])
            else:
                sum_map[summ] = i
                
            # print(sum_map)
            
        return res
            