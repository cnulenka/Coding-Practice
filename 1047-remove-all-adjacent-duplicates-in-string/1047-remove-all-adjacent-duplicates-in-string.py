class Solution:
    def removeDuplicates(self, s: str) -> str:
        
        st = [s[0]]
        flag = False
        i = 1
        
        while i < len(s):
            if st and st[-1] == s[i]:
                st.pop()
                i=i+1
                #print(i, s[i], st, flag)
                #print("hola1")
                #while  i < len(s) and st[-1] == s[i]:
                #    flag = True
                #    i+=1
                #if flag:
                #    st.pop()
                #    flag = False
                #print(i, s[i], st, flag)
            else:
                #print(i, s[i], st, flag)
                #print("hola2")
                st.append(s[i])
                #print(i, s[i], st, flag)
                i+=1
        
        return "".join(st)