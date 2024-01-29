class Solution {

    private void getAllSubsets(int[] nums, int index, List<Integer> currList, List<List<Integer>> res) {
        if(index == nums.length) {
            res.add(new ArrayList<>(currList));
            return;
        }

        // include
        currList.add(nums[index]);
        getAllSubsets(nums, index+1, currList, res);
        currList.remove(currList.size()-1);
        // exclude
        getAllSubsets(nums, index+1, currList, res);
    }

    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        getAllSubsets(nums, 0, new ArrayList<>(), res);
        return res;
    }
}