class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        res = high
        
        while low <= high: 
            speed = low + (high-low)//2
            # print(low, speed, high)
            
            hours = 0
            
            for pile in piles:
                hours += math.ceil(pile/speed)
            
            if hours <= h:
                res = min(speed, res)
                # speed is too high, decrease speed
                # we are aiming for the lowest successful
                high = speed - 1
            else:
                # speed is too low, increase speed
                low = speed + 1
        
        return res
        
        