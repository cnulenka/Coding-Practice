class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        ans = base = end = 0
        
        while base < n:
            end = base
            
            if end + 1 < n and arr[end] < arr[end+1]:
                
                while end + 1 < n and arr[end] < arr[end+1]:
                    end += 1
                    
                if end + 1 < n and arr[end] > arr[end+1]:
                    
                    while end + 1 < n and arr[end] > arr[end+1]:
                        end += 1
                        
                    ans = max(ans, end-base +1)
            
            base = max(end, base+1)
        
        
        return ans