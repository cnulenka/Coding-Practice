class Solution {

    List<List<Integer>> res;

    private void swap(int[] nums, int i, int j){
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }

    private void solve(int index, int[] nums) {

        if(index == nums.length){
            res.add(new ArrayList<>(Arrays.stream(nums).boxed().collect(Collectors.toList()))); // O(N)
            return;
        }

        for(int i = index; i < nums.length; i++){
            swap(nums, i, index);
            solve(index + 1, nums);
            swap(nums, i, index);
        }
    }

    public List<List<Integer>> permute(int[] nums) {
        res = new ArrayList<>();
        solve(0, nums);
        return res;
    }
}