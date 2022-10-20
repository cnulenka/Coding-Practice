class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        n = len(nums)
        
        def permute(perm, counter):
            nonlocal res, n
            
            if len(perm) == n:
                res.append(list(perm))
                return
            
            for num in counter:                
                if counter[num]:
                    counter[num] -= 1
                    perm.append(num)
                    permute(perm, counter)
                    counter[num] += 1
                    perm.pop()
        
        permute([], Counter(nums))
        return res