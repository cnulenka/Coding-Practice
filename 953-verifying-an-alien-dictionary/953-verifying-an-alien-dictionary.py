class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = {}
        
        for i,c in enumerate(order):
            order_map[c] = i
        
        # only compare consecutive words
        # if consecutive words are sorted
        # array is sorted.
        
        for i in range(len(words) - 1):
            
            # loop over ith word, if it has more chars we can check
            for j in range(len(words[i])):
                
                if j >= len(words[i+1]):
                    return False
                
                if words[i][j] != words[i+1][j]: # only check letter that are different
                    if order_map[words[i][j]] > order_map[words[i+1][j]]:
                        return False
                    
                    # we dont need to examine rest 
                    # tricky
                    break
        
        return True