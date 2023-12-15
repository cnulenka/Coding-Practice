class Solution {
    public int trap(int[] height) {
        int l = 0, r = height.length - 1, water = 0, lMax = 0, rMax = height.length - 1;
        // So, we can say that if there is a larger bar at one end (say right), we are assured that the water trapped would be dependant on height of bar in current direction (from left to right). As soon as we find the bar at other end (right) is smaller, we start iterating in opposite direction (from right to left).
        while (l<r){
            if(height[l] < height[r]){
                if(height[lMax] < height[l]){
                    lMax = l;
                }
                water += height[lMax] - height[l];
                l++;
            } else {
                if(height[rMax] < height[r]){
                    rMax = r;
                }
                water += height[rMax] - height[r];
                r--;
            }
        }

        return water;
    }
}