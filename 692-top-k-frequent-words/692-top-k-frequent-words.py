class HeapEle:
    
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq
        
    def __lt__(self, other):
        #print(self.freq, other.freq, self.word, other.word)
        if self.freq == other.freq:
            return self.word > other.word
        return self.freq < other.freq
    
    def __str__(self):
        return self.word + " "+ str(self.freq)

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = defaultdict(int)
        
        for word in words:
            freq[word] += 1
            
        #print("n">"love")
            
        heap = []
        
        for key,v in freq.items():
            #print(heap)
            heapq.heappush(heap, HeapEle(key, v))
            
            if len(heap) > k:
                heapq.heappop(heap)
        #print(heap)
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap).word)
        return res[::-1]
        
        