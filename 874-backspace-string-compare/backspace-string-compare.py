class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        ss=[]

        for i in s:
            if i=="#" and ss:
                ss.pop()
            elif i!="#":
                ss.append(i)
        ress="".join(ss)

        st=[]
        for j in t:
            if j=="#" and st:
                st.pop()
            elif j!="#":
                st.append(j)
        rest="".join(st)

        return rest==ress
        