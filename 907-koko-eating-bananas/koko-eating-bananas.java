class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int left = 0, right = 0;
        for(int pile: piles){
            right = Math.max(right, pile);
        }
        int res = right;

        while(left <= right){
            int mid = (right-left)/2 + left;

            int time = 0;
            //System.out.println("mid: "+mid);
            for(int pile: piles){
                double dpile = pile;
                time += Math.ceil(dpile/mid);
            }
            //System.out.println("time: "+time);

            if(time <= h){
                res = mid;
                right = mid - 1;
            } else{
                left = mid + 1;
            }
        }

        return res;
    }
}