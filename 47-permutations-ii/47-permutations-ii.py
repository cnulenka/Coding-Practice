class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(perm, counter):
            
            if len(perm) == len(nums):
                res.append(list(perm))    
            
            for num in counter:
                if counter[num]:
                    counter[num] -= 1
                    perm.append(num)
                    backtrack(perm, counter)
                    counter[num] += 1
                    perm.pop()
           
        
        res = []
        backtrack([], Counter(nums))
        return res
        