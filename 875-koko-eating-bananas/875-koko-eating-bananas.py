class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        
        while low < high: # <= leads to TLE # tricky
            speed = low + (high-low)//2
            
            hours = 0
            
            for pile in piles:
                hours += math.ceil(pile/speed)
            
            if hours <= h:
                # speed is too high, decrease speed
                high = speed
            else:
                # speed is too low, increase speed
                low = speed + 1
        
        return high
        
        