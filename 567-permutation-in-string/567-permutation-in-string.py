class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        n1 = len(s1)
        n2 = len(s2)
        
        if n2 < n1:
            return False
        
        s1_counter = [0 for _ in range(26)]
        s2_counter = [0 for _ in range(26)]
        
        for i in range(n1):
            s1_counter[ord(s1[i]) - ord('a')] += 1
            s2_counter[ord(s2[i]) - ord('a')] += 1
        
        if s1_counter == s2_counter:
            return True
        
        l = 0
        for i in range(n1, n2):
            
            s2_counter[ord(s2[l]) - ord('a')] -= 1
            s2_counter[ord(s2[i]) - ord('a')] += 1
            l+=1
            
            if s1_counter == s2_counter:
                return True
        
        
        return False
            
            