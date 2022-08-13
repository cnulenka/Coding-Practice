class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        heap = []
        
        for i,point in enumerate(points):
            x=point[0]
            y=point[1]
            dist = -(x**2 + y**2)
            # print(dist)
            if i < k:
                heapq.heappush(heap, (dist, x, y))
            else:
                if heap[0][0] < dist:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (dist, x, y))
        
        return [[point[1], point[2]] for point in heap]
            