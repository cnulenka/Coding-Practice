#User function Template for python3

class Solution:
    #Function to return k largest elements from an array.
    def kLargest(self,li,n,k):
        import heapq
        
        temp_list = []
        
        for i in range(k):
            temp_list.append(li[i])
        
        heapq.heapify(temp_list)
        
        for i in range(k, n):
            top = heapq.heappop(temp_list)
            if li[i] > top:
                heapq.heappush(temp_list, li[i])
            else:
                heapq.heappush(temp_list, top)
        
        res = []
        
        while temp_list:
            res.append(heapq.heappop(temp_list))
        
        res.reverse()
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