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
            // if(i > 0 && nums[i] == nums[i-1]){
            //     continue;
            // }

            // i > index not i > 0
            // we need to include index atleast
            // so > 0 will fail
            // 1, 2 will not become 1, 2, 2
            if(i > index && nums[i] == nums[i-1]){
                continue;
            }
            currList.add(nums[i]);
            getAllSubsets(nums, i+1, currList, res);
            currList.remove(currList.size()-1);
        }
    }

    public List<List<Integer>> subsetsWithDup(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        Arrays.sort(nums);
        getAllSubsets(nums, 0, new ArrayList<>(), res);
        return res;
    }
}