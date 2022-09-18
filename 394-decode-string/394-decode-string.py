class Solution:
    def decodeString(self, s: str) -> str:
        count_stack = []
        string_stack = []
        curr_str = ""
        curr_num = ""
        decoded_str = ""
        
        for c in s:
            if c >= '0' and c <= '9':
                curr_num += c
            elif c == '[':
                count_stack.append(int(curr_num))
                string_stack.append(curr_str)
                curr_str = ""
                curr_num = ""
            elif c == ']':
                num = count_stack.pop()
                decoded_str = string_stack.pop()
                decoded_str += num*curr_str
                curr_str = decoded_str
            else:
                curr_str += c
                
        return curr_str