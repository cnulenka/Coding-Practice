

class Solution:
    
    #Function to find the minimum number of swaps required to sort the array.
	def minSwaps(self, nums):
	    n = len(nums)
		arrpos = [*enumerate(nums)]
		arrpos.sort(key = lambda x:x[1])
		
		
		vis = { i: False for i in range(n)}
		ans = 0 
		
		
		for i in range(n):
		    
		    if vis[i] or arrpos[i][0] == i:
		        continue
		    
		    
		    j = i
		    cycle_size = 0
		    
		    while not vis[j]:
		        
		        vis[j] = True
		        j = arrpos[j][0]
		        
		        cycle_size += 1
		    
		    if cycle_size > 0:
		        ans += cycle_size - 1
		     
		 
		return ans

#{ 
#  Driver Code Starts


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		nums = list(map(int, input().split()))
		obj = Solution()
		ans = obj.minSwaps(nums)
		print(ans)

# } Driver Code Ends