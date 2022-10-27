class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        heap = []
        num_freq = Counter(nums)
        
        for num, freq in num_freq.items():
            heapq.heappush(heap, (freq, num))
            
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [_[1] for _ in heap]
            
            
            