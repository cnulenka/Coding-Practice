class Solution {

    private void solve(int index, int[] candidates, int target, List<Integer> currList, List<List<Integer>> res) {

        if(target < 0){
            return;
        }

        if(target == 0){
            res.add(new ArrayList<>(currList));
            return;
        }

        for(int i = index; i < candidates.length; i++){
            currList.add(candidates[i]);
            solve(i, candidates, target - candidates[i], currList, res);
            currList.remove(currList.size() - 1);
        }
    }

    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        
        List<List<Integer>> ans = new ArrayList();
        solve(0, candidates, target, new ArrayList(), ans);
        return ans;
    }
}