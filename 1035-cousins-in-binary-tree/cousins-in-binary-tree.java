/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean isCousins(TreeNode root, int x, int y) {
        Queue<Pair<TreeNode, TreeNode>> queue = new LinkedList<>();
        queue.offer(new Pair<TreeNode, TreeNode>(root, root));

        while(!queue.isEmpty()){
            Integer size = queue.size();
            Boolean xFound = false;
            TreeNode xParent = null;
            Boolean yFound = false;
            TreeNode yParent = null;
            for(int  i = 0;  i < size; i++) {
                Pair<TreeNode, TreeNode> front = queue.poll();
                if(front.getKey().val == x){
                    xFound = true;
                    xParent = front.getValue();
                } else if(front.getKey().val == y){
                    yFound = true;
                    yParent = front.getValue();
                }

                if(xFound && yFound && (xParent.val != yParent.val)) {
                    return true;
                }

                if(front.getKey().left != null){
                    queue.offer(new Pair<TreeNode, TreeNode>(front.getKey().left, front.getKey()));
                }
                if(front.getKey().right != null){
                    queue.offer(new Pair<TreeNode, TreeNode>(front.getKey().right, front.getKey()));
                }
            }
        }

        return false;
    }
}