class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        
        res = []
        
        def comb(digit, digit_ind, curr_num):
            
            if digit_ind == n - 1:
                # print(digit, digit_ind, curr_num)
                res.append(curr_num)
                return
            
            if digit + k < 10:
                new_num = curr_num * 10 + digit + k
                comb(digit + k, digit_ind+1, new_num)
            
            if digit - k >= 0 and k != 0:
                new_num = curr_num * 10 + digit - k
                comb(digit - k, digit_ind+1, new_num)
        
        
        
        for i in range(1, 10):
            comb(i, 0, i)
            
        return res