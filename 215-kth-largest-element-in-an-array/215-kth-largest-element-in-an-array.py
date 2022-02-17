class Solution:
    def findKthLargest(self, nums, k):

        def partition(left, right):
            
            pivot_index = left
            
            for i in range(left, right):
                if nums[i] < nums[right]:
                    nums[pivot_index], nums[i] = nums[i], nums[pivot_index]
                    pivot_index += 1
            
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
            
            return pivot_index           
        
        def select(left, right, k):
            
            if left == right:      
                return nums[left] 
            
            partiton_index = partition(left, right)
            
            if partiton_index == k:
                return nums[k]
            elif partiton_index < k:
                return select(partiton_index+1, right, k)
            else:
                return select(left, partiton_index-1, k)  

        return select(0, len(nums) - 1, len(nums) - k)