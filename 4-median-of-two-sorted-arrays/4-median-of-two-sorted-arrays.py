class Solution:
    def findMedianHelper(self, nums1, nums2, m, n):
        if m>n:
            return self.findMedianHelper(nums2, nums1, n, m)
        
        low = 0
        high = m # important not m - 1 
        median = (m + n + 1)//2
        
        while low <= high:
            
            cut1 = (low + high)//2
            cut2 = median - cut1
            
            
            l1 = float('-inf') if cut1 == 0 else nums1[cut1-1]
            l2 = float('-inf') if cut2 == 0 else nums2[cut2-1]
            r1 = float('inf') if cut1 == m else nums1[cut1]
            r2 = float('inf') if cut2 == n else nums2[cut2]
            
        
            
            
            if l1 <= r2 and l2 <= r1:
                if (m+n)%2 != 0:
                    return max(l1,l2)
                return (max(l1,l2) + min(r1,r2))/2
            
            if l1 > r2:
                high = cut1 - 1
            else:
                low = cut1 + 1
        
        return 0.0
            
        
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        return self.findMedianHelper(nums1, nums2, len(nums1), len(nums2))