class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        char_stk = [s[0]]
        num_stk = [1]
        
        for i in range(1, len(s)):
            
            # check if last k-1 letters
            # are same as curr char
            
            # print(char_stk, num_stk, i, s[i])

            if char_stk and char_stk[-1] == s[i]:
                
                if num_stk[-1] == k - 1:

                    while num_stk[-1]:
                        char_stk.pop()
                        num_stk[-1] -= 1

                    num_stk.pop()
                else:
                    num_stk[-1] += 1
                    char_stk.append(s[i])
            else:
                num_stk.append(1)
                char_stk.append(s[i])
        
        return "".join(char_stk)