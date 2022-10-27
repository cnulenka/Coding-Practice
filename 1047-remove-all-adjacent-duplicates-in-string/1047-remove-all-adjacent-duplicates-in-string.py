class Solution:
    def removeDuplicates(self, s: str) -> str:
        
        st = []
        n = len(s)
        i = 0
        
        while i < n:
            
            if st and s[i] == st[-1]:
                    st.pop()
            else:
                st.append(s[i])
                    
            i += 1
            # print(st, i)
            
        return "".join(st)
        