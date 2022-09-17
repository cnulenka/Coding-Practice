class CustomComparator(str):
    
    def __lt__(x,y):
        if x+y < y+x:
            return False
        return True

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        res = "".join(sorted(nums, key=CustomComparator))
        if res[0] == '0':
            return "0"
        return res