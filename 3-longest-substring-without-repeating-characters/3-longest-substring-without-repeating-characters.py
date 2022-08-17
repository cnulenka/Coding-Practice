class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        max_length = 0
        dic = defaultdict(int)
        l=0
        r=0
        
        while r < len(s):
            #print(dic)
            
            if not dic[s[r]]:
                dic[s[r]] += 1
                #print(r-l+1)
                max_length = max(max_length, r-l+1)
            else:
                 while dic[s[r]] and l<=r:
                    dic[s[l]] -= 1
                    l += 1
                 dic[s[r]] += 1
            r+=1
            
        return max_length
            
            
            
            
        