class Solution {
    public String decodeString(String s) {
        Stack<Integer> numStack = new Stack<>();
        Stack<String> strStack = new Stack<>();
        int currNum = 0;
        StringBuilder currStr = new StringBuilder();
        for(char c : s.toCharArray()) {
            if( Character.isDigit(c)){
                currNum = currNum*10 + c - '0';
            } else if ( c == '['){
                numStack.push(currNum);
                strStack.push(currStr.toString());
                currNum = 0;
                currStr = new StringBuilder();
            } else if (c == ']'){
                Integer lastNum = numStack.pop();
                StringBuilder lastStr = new StringBuilder(strStack.pop());
                
                for(int j = 0; j< lastNum; j++){
                    lastStr.append(currStr.toString());
                }
                currStr = lastStr;
            } else {
                currStr.append(c);
            }
        }

        return currStr.toString();
    }
}