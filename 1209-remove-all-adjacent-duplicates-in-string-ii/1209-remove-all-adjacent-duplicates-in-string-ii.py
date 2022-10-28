class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        char_stk = ['#']
        num_stk = [0]
        
        for c in s:
            
            # check if last k-1 letters
            # are same as curr char
            
            # print(char_stk, num_stk)
                
            if char_stk[-1] == c and num_stk[-1] == k - 1:

                    pop_count = num_stk[-1]

                    while pop_count:
                        char_stk.pop()
                        num_stk.pop()
                        pop_count -= 1

                    continue
                
            
            if char_stk[-1] == c:
                num_stk.append(num_stk[-1] + 1)
            else:
                num_stk.append(1)

            char_stk.append(c)
        
        char_stk = char_stk[1:]
        return "".join(char_stk)