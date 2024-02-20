class Solution {
    int[] dp;

    /*
    Hence, there could be 2^N possible substrings in the worst case. For each substring, 
    it takes O(N) time to generate the substring and determine if it is a palindrome or not. 
    This gives us a time complexity of O(N⋅2^N)
    */
 
    public boolean isPalindrome(String s, int low, int high){
        while(low < high)
            if(s.charAt(low++) != s.charAt(high--)) return false;
        return true;
    } 

    private int solve(int ind, String s){

        if(ind == s.length()) {
            return 0;
        }

        if(dp[ind] != -1){
            return dp[ind];
        }

        int minCost = Integer.MAX_VALUE;
        for(int i = ind; i < s.length(); i++) {
            if(isPalindrome(s, ind, i)){
                int cost = 1 + solve(i+1, s);
                minCost = Math.min(minCost, cost);
            }
        }

        dp[ind] = minCost;
        return minCost;
    }

    public int minCut(String s) {
        dp = new int[s.length()+1];
        Arrays.fill(dp, -1);
        return solve(0, s) - 1;    
    }
}