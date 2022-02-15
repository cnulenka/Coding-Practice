class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        start = 0
        end = len(nums) - 1
        count = 0
        
        while start <= end:
            #mid = (start + (end-start))//2
            mid = (start + end) //2
            #print(start, mid, end)
            
            #count +=1
            
            #if count == 100:
            #    break
            
            if (mid == 0 or nums[mid] < nums[mid - 1]) and (mid==len(nums)-1 or nums[mid] < nums[mid+1]):
                return nums[mid]
            else:
                #print("hola")
                if nums[mid] >= nums[0] and nums[mid] >= nums[-1]:
                    #print("hola1")
                    start = mid + 1
                else:
                    #print("hola2")
                    end = mid - 1
        
        
        return -1
                    