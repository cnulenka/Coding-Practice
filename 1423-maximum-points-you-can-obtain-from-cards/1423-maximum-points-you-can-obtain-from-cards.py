class Solution:
    def maxScore(self, cp: List[int], k: int) -> int:
        curr_score = 0
        
        for i in range(k):
            curr_score += cp[i]
            
        max_score = curr_score
        t = k-1
        for i in range(len(cp)-1, len(cp)-k-1, -1):
            #print(i,t)
            curr_score = curr_score - cp[t] + cp[i]
            max_score = max(max_score, curr_score)
            t-=1
        
        return max_score