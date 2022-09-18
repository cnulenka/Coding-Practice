class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x:x[0])
        
        remove = 0
        prev = 0
        
        for i in range(1, len(intervals)):
            if intervals[prev][1] > intervals[i][0]:
                # trick
                # which ever has longer ending we remove
                # it
                if intervals[prev][1] > intervals[i][1]:
                    prev=i
                remove += 1
            else:
                prev=i
                
        return remove