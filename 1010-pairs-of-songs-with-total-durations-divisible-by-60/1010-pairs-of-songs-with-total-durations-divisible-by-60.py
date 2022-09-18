class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        remainders = defaultdict(int)
        pairs = 0
        
        for t in time:
            if t%60 == 0:
                pairs += remainders[0]
            else:
                pairs += remainders[60 - t%60]
            
            remainders[t%60] += 1
        
        return pairs