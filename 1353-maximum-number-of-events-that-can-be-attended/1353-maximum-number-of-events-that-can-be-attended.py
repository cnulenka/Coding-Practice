class SortEventTime(list):
    
    def __lt__(x,y):
        
        if x[0] == y[0]:
            # if start date equal
            # sort by end date
            return x[1] < y[1]
        
        # sort it by start date
        return x[0] < y[0]

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events = sorted(events, key=SortEventTime)
        
        n = len(events)
        i = 0
        d = 1
        count = 0
        pq = []
        
        while i<n or pq:
            if not pq:
                d = events[i][0]
            
            # id start date is less than equal to curr_date
            # push the event's end date
            while i < n and events[i][0] <= d: # push all events we can possibly attend
                # push the end dates
                heapq.heappush(pq, events[i][1])
                i += 1
            
            heapq.heappop(pq) # attend this event that ends soonest
            d += 1 # increment the day
            count += 1
            
            while pq and pq[0] < d: # remove all impossible-to-attend events
                heapq.heappop(pq)
                
        return count
        
            