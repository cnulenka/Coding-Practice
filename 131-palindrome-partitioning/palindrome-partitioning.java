class Solution {

    List<List<String>> res;

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

    private void solve(int ind, String s, List<String> currList){

        if(ind == s.length()) {
            res.add(new ArrayList<>(currList));
            return;
        }

        for(int i = ind; i < s.length(); i++) {
            if(isPalindrome(s, ind, i)){
                currList.add(s.substring(ind, i+1));
                solve(i+1, s, currList);
                currList.remove(currList.size() - 1);
            }
        }
    }

    public List<List<String>> partition(String s) {
        res = new ArrayList<>();
        solve(0, s, new ArrayList<>());
        return res;       
    }
}