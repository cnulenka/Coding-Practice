class Solution:
    def reorganizeString(self, s: str) -> str:
        freq_map = collections.Counter(s)
        max_heap = []
        for char, freq in freq_map.items():
            max_heap.append([-freq, char])
        heapq.heapify(max_heap) #O(n)
        
        res = ""
        #print(max_heap)
        while max_heap:
            
            max_char = heapq.heappop(max_heap)
            
            if len(max_heap) == 0:
                if (max_char[0] * -1) > 1:
                    return ""
                else:
                    res += max_char[1]
                    return res
            
            second_max_char = heapq.heappop(max_heap)
            
            res += max_char[1] + second_max_char[1]
            
            max_char[0] += 1
            second_max_char[0] += 1
            
            if max_char[0] != 0:
                heapq.heappush(max_heap, max_char)
            
            if second_max_char[0] != 0:
                heapq.heappush(max_heap, second_max_char)
        
        return res
                
            
            
                
        