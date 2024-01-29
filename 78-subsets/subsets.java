class Solution {

    private void getAllSubsets(int[] nums, int index, List<Integer> currList, List<List<Integer>> res) {

        // used in backtracking
        res.add(new ArrayList<>(currList));
        if(index == nums.length) {
            return;
        }
        
        // used when include and exclude

        // if(index == nums.length) {
        //     res.add(new ArrayList<>(currList));
        //     return;
        // }

        for(int i = index; i < nums.length; i++){
            currList.add(nums[i]);
            getAllSubsets(nums, i+1, currList, res);
            currList.remove(currList.size()-1);
        }
    }

    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        getAllSubsets(nums, 0, new ArrayList<>(), res);
        return res;
    }
}