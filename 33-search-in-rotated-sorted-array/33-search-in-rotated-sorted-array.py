class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        start = 0
        end = len(nums) - 1
        count = 0
        
        while start <= end:
            #if count == 5:
            #    break
            #else:
            #    count += 1
            mid = start + (end - start)//2
            #print(start, mid, end)
            if nums[mid] == target:
                return mid
            elif nums[0] < nums[-1]:
                if target > nums[mid]:
                    start = mid + 1
                else:
                    end = mid - 1
            elif nums[mid] >= nums[0] and nums[mid] >= nums[-1]:
                if target < nums[mid] and target >= nums[0]:
                    end = mid - 1
                else:
                    start = mid + 1
            elif nums[mid] <= nums[0] and nums[mid] <= nums[-1]:
                if target > nums[mid] and target <= nums[-1]:
                    start = mid + 1
                else:
                    end = mid - 1
        
        return -1