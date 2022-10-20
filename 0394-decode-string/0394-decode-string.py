class Solution:
    def decodeString(self, s: str) -> str:
        
        num_stack = []
        str_stack = []
        
        
        curr_str = ""
        curr_num = ""
        
        
        for c in s:
            
            if c >= '0' and c <= '9':
                curr_num += c
            elif c == "[":
                num_stack.append(curr_num)
                str_stack.append(curr_str)
                curr_num = ""
                curr_str = ""
            elif c == "]":
                
                last_num = num_stack.pop()
                last_str = str_stack.pop()
                
                last_str += curr_str*int(last_num)
                curr_str = last_str
    
            else:
                curr_str += c
                
        return curr_str
        
        
        