class Solution:
    def numSquares(self, n: int) -> int:
        
        # exactly minimum coins, coin change problem
        
        # why are we going till root n
        squares = [i*i for i in range(1, int(math.sqrt(n)) + 1)]
        # print(squares)
        
        dp = [float('inf') for i in range(n+1)]
        
        dp[0] = 0
        
        for i in range(n+1): # O(n)
            for square in squares: # (root(n))
                
                # break if square is bigger than i
                if i < square:
                    break
                dp[i] = min(dp[i], dp[i-square] + 1)
                
        return dp[n]
        
        