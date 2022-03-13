#User function Template for python3

class Solution:
    #Function to return k largest elements from an array.
    def kLargest(self,li,n,k):
        import heapq
        
        temp_list = []
        
        for i in range(k):
            temp_list.append(li[i])
        
        heapq.heapify(temp_list) # O(k)
        
        for i in range(k, n): # O(n * logk)
            if li[i] > temp_list[0]:
                heapq.heappop(temp_list)
                heapq.heappush(temp_list, li[i])
        
        res = []
        
        while temp_list: # O(klogk)
            res.append(heapq.heappop(temp_list))
        
        res.reverse() # O(k)
        return res
         

#{ 
#  Driver Code Starts
#Initial Template for Python 3

t=int(input())
for _ in range(t):
    li = [int(x) for x in input().strip().split()]
    n=li[0]
    k=li[1]
    li = [int(x) for x in input().strip().split()]
    ob=Solution()
    k_largest_list = ob.kLargest(li,n,k)
    
    for element in k_largest_list:
        print(element, end = ' ')
    print('')
# } Driver Code Ends