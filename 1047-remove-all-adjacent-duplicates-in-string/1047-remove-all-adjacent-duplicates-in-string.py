class Solution:
    def removeDuplicates(self, s: str) -> str:
        
        st = [s[0]]
        flag = False
        i = 1
        
        while i < len(s):
            if st and st[-1] == s[i]:
                st.pop()
                i=i+1
            else:
                st.append(s[i])
                i+=1
        
        return "".join(st)