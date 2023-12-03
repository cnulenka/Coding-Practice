class Solution {
    List<List<Integer>> res;
    private void computeCombSum(int currIndex, int target, int[] candidates, List<Integer> currList) {

        if (currIndex == candidates.length || target<0) {
            return;
        }

        if(target == 0) {
            res.add(new ArrayList<>(currList));
            return;
        }

        currList.add(candidates[currIndex]);
        computeCombSum(currIndex, target - candidates[currIndex], candidates, currList); // inlcude
        currList.remove(currList.size()-1);
        computeCombSum(currIndex+1, target, candidates, currList); // exclude
    }
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        res = new ArrayList<>();
        computeCombSum(0, target, candidates, new ArrayList<>());
        return res;
    }
}