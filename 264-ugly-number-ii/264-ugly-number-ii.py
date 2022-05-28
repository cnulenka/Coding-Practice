class Solution:
    def nthUglyNumber(self, n: int) -> int:
        
        if n <= 1:
            return n
        
        p2 = 0
        p3 = 0
        p5 = 0
        
        k = [0]*n
        k[0] = 1
        
        for i in range(1,n):
            k[i] = min(k[p2]*2, min(k[p3]*3, k[p5]*5))
            if k[i] == k[p2]*2:
                p2+=1 
            if k[i] == k[p3]*3:
                p3+=1 
            if k[i] == k[p5]*5:
                p5+=1 
        
        return k[-1]
            