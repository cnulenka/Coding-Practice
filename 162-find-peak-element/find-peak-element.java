class Solution {
    public int findPeakElement(int[] a) {
        int l = 0, r = a.length - 1, n  = a.length;
        if (n == 1) {
            return 0;
        }

        while (l<=r) {
            int mid = l  + (r-l)/2;

            if((mid == n-1  || a[mid] > a[mid+1]) && (mid == 0 || a[mid] > a[mid-1])){
                return mid;
            }

            if(a[mid+1] > a[mid]){
                l = mid+1;
            } else {
                r = mid - 1;
            }
        }

        return 0;
    }
}