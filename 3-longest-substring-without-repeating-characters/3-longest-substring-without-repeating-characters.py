class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if not s:
            return 0
        
        max_length = 1
        freq = {}
        left = 0
        
        freq[s[0]] = 0
        
        for i in range(1, len(s)):
            if s[i] in freq:
                left = max(left, freq[s[i]] + 1)
            
            max_length = max(max_length, i - left + 1)
            freq[s[i]] = i
        
        return max_length