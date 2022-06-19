class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        sorted_list = sorted(pairs, key = lambda x: x[1])
        
        curr = float(-inf)
        ans = 0
        
        for p in sorted_list:
            if curr < p[0]:
                curr = p[1]
                ans += 1
                
        return ans