from sortedcontainers import SortedList

class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        
        busy, free = [], SortedList(list(range(k)))
        count = [0 for _ in range(k)]
        
        
        for i in range(len(arrival)):
            #print(free, busy, "before")
            
            while busy and arrival[i] >= busy[0][0]:
                _, _id = heapq.heappop(busy)
                free.add(_id)
                
            #print(free, busy, "after")
            if free:
                _id = free.bisect_left(i%k)
                busy_id = free[_id] if _id < len(free) else free[0]
                free.remove(busy_id)
                count[busy_id] += 1
                heapq.heappush(busy, (load[i]+arrival[i], busy_id))
                
        
        max_load = max(count)
        res = []
        
        for i in range(k):
            if count[i] == max_load:
                res.append(i)
                
        return res