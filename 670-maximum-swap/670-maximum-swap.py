class Solution:
    def maximumSwap(self, num: int) -> int:
        
        last_index = [0 for _ in range(10)]
        
        nums = list(str(num))
        n = len(nums)
        for i in range(n):
            #print(num[i])
            last_index[ord(nums[i]) - ord('0')] = i
        
        for i in range(n):
            # print(nums[i])
            for digit in range(9, -1, -1):
                curr_digit = ord(nums[i]) - ord('0')
                #print(digit > curr_digit, digit , curr_digit, last_index[digit], i)
                if digit > curr_digit and last_index[digit] > i:
                    #print(num[i], num[dp[ord(num[i]) - ord('0')]])
                    nums[i], nums[last_index[digit]] = nums[last_index[digit]], nums[i]
                    return ''.join(nums)
        
        return ''.join(nums)
        