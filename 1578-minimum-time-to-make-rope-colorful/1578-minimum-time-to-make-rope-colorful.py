class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        prev_char = '*'
        prev_cost = 0
        res = 0
        for i in range(len(colors)):
            if colors[i] == prev_char:
                if prev_cost < neededTime[i]:
                    res += prev_cost
                    prev_cost = neededTime[i]
                else:
                    res += neededTime[i]
            else:
                prev_char = colors[i]
                prev_cost = neededTime[i]
        
        return res