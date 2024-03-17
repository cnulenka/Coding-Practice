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
    /*
    Let N be the number of candidates, T be the target value, and M be the minimal value among the candidates.

    Time Complexity: O(N^(T/M+1))

        As we illustrated before, the execution of the backtracking is unfolded as a DFS traversal in a n-ary tree.
        The total number of steps during the backtracking would be the number of nodes in the tree.

        At each node, it takes a constant time to process, except the leaf nodes which could take a linear time 
        to make a copy of combination. 
        So we can say that the time complexity is linear to the number of nodes of the execution tree.

        Here we provide a loose upper bound on the number of nodes.

            First of all, the fan-out of each node would be bounded to N, i.e. the total number of candidates.

            The maximal depth of the tree, would be T/M​, where we keep on adding the smallest 
            element to the combination.

            As we know, the maximal number of nodes in N-ary tree of T/M​ height would be O(N^(T/M+1)).
*/
}