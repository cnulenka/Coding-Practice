class Solution:
    def minDeletions(self, s: str) -> int:
        freq = [0] * 26
        for c in s:
            freq[ord(c) - ord('a')] += 1
            
        freq.sort(reverse=True)
        
        max_freq = len(s)
        delete_count = 0
        
        for f in freq:
            if f > max_freq:
                delete_count += f - max_freq
                f = max_freq
                
            max_freq = max(f - 1, 0) 
            
        
        return delete_count