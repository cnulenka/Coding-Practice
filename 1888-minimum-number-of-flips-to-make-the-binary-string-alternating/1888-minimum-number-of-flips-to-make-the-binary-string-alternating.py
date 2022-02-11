class Solution:
    def minFlips(self, s: str) -> int:
        gcount = 0
        lcount = 0
        oc = len(s)
        s = s+s
        
        from collections import defaultdict
        dic = defaultdict(int)
        
        for i in range(len(s)//2):

            if i%2 == 0 and s[i] == '1':
                dic[i] = 1
                lcount += 1
            
            if i%2 == 1 and s[i] == '0':
                dic[i] = 1
                lcount += 1
        

        gcount= min(lcount, len(s)//2 - lcount)
        
        st = 1
        e = oc
        
        while e <= len(s) - 1:
            ce = 0
            
            if e%2 == 0 and s[e] == '1':
                ce += 1

            if e%2 == 1 and s[e] == '0':
                ce += 1
            
            lcount = lcount - dic[st-1] + ce
            dic[e] = ce
            gcount= min(gcount, min(lcount, len(s)//2 - lcount))
            
            st += 1
            e += 1
        
        return gcount
                
                