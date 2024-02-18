class NodeInfo {
    public int min;
    public int max;
    public int sum;
    public boolean isBST; 

    public NodeInfo(int sum, boolean isBST, int min, int max) {
        this.min = min;
        this.max = max;
        this.sum = sum;
        this.isBST = isBST;
    }
}

class Solution {

    private int maxSum;

    public NodeInfo solve(TreeNode root){
        if(root == null){
            return new NodeInfo(0, true, Integer.MAX_VALUE, Integer.MIN_VALUE);
        }

        NodeInfo left = solve(root.left);
        NodeInfo right = solve(root.right);
        if(left.isBST && right.isBST && left.max < root.val  && right.min > root.val) {
            int sum = root.val + left.sum + right.sum;
            maxSum = Math.max(maxSum, sum);
            return new NodeInfo(sum, true, Math.min(left.min, root.val), Math.max(right.max, root.val));
        }

        return new NodeInfo(0, false, Integer.MAX_VALUE, Integer.MIN_VALUE);
    }

    public int maxSumBST(TreeNode root) {
        maxSum = 0;
        solve(root);
        return maxSum;
    }
}