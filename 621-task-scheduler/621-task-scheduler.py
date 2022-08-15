class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        # official solution is NOT intuitive
        # this code is taken from Neetcode
        
        count = Counter(tasks)
        max_heap = [-val for val in count.values()]
        heapq.heapify(max_heap)  
        
        q = deque()
        
        time = 0
        
        while max_heap or q: # O(len(tasks) * n) at max
            
            time +=1 
            
            if max_heap:
                top = 1+ heapq.heappop(max_heap) # we have to reduce, hence + 1 # O(log26) constant
                if top: # only if positive 
                    q.append([top, time+n]) # decrease count and append next time slot
            
            # if front of q has current time
            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0]) # O(log26) constant
        
        return time
        