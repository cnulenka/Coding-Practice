class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        count_stack = [1]
        char_stack = [s[0]]
        
        for i in range(1,len(s)):
            #print(count_stack, char_stack)
            if not char_stack or (char_stack and s[i] != char_stack[-1]):
                count_stack.append(1)
                char_stack.append(s[i])
            elif count_stack[-1]+1 == k:
                while count_stack[-1]:
                    char_stack.pop()
                    count_stack[-1] -= 1
                count_stack.pop()
            else:
                count_stack[-1] += 1
                char_stack.append(s[i])
        
        return "".join(char_stack)
                
                    