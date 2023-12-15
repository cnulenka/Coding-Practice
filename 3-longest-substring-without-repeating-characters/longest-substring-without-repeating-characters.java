class Solution {
    public int lengthOfLongestSubstring(String s) {
        Map<Character, Integer> charMap = new HashMap<>();
        int longestSubstring = 0, left = 0, right = 0;
        while(right <  s.length()){
            Character currChar = s.charAt(right); 
            if(charMap.containsKey(currChar)) {
                int prevOccurence = charMap.get(currChar);
                while(left <= prevOccurence) {
                    charMap.remove(s.charAt(left));
                    left+=1;
                }
            }
            charMap.put(currChar, right);
            longestSubstring = Math.max(longestSubstring, right - left + 1);
            right += 1;
        }

        return longestSubstring;
    }
}