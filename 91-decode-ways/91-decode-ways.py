class Solution:
    def numDecodings(self, s: str) -> int:
        
        def num_ways(index):
            nonlocal dic
            if index in dic:
                return dic[index]
            
            if index == len(s):
                return 1

            if s[index] == '0':
                return 0
            
            if index == len(s) -1:
                return 1
            
            ways = num_ways(index+1)
            if 10 <= int(s[index:index+2]) <= 26:
                ways += num_ways(index+2)
            
            dic[index] = ways
            return ways
    
        
        dic = {}
        return num_ways(0)