class LargerNumKey(str):
    
    def __lt__(x,y):
        return x+y > y+x

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        str_nums = list(map(str, nums))
        
        desc_sorted_nums = sorted(str_nums, key=LargerNumKey)

        largest_num = ''.join(desc_sorted_nums)
        
        if largest_num[0] == '0':
            return "0"
        else:
            return largest_num