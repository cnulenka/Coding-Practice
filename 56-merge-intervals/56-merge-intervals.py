class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x:x[0])
        res = [intervals[0]]
        # print(intervals)
        
        for i in range(len(intervals)):
            if res[-1][1] >= intervals[i][0]:
                # trick take max of both ends
                res[-1][1] = max(res[-1][1],intervals[i][1])
            else:
                res.append(intervals[i])
        
        return res
            
        