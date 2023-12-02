class Solution {
    public int[] fairCandySwap(int[] aliceSizes, int[] bobSizes) {
        // alice gives x, bob gives y
        // Sa + y -  x = Sb + x - y
        // y = (Sb-Sa)/2 + x

        int sa = 0, sb = 0;
        Set<Integer> set = new HashSet<>();
        for(int x: aliceSizes){
            sa +=x;
        }
        for(int y: bobSizes){
            sb +=y;
            set.add(y);
        }

        int delta = (sb-sa)/2;
        for(int x: aliceSizes){
            if(set.contains(x+delta)){
                return new int[]{x, x+delta};
            }
        }

        return null;
    }
}