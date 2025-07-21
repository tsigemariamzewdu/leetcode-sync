class Solution:
    def makeFancyString(self, s: str) -> str:
        res=[s[0]]
        count=1
        current=s[0]
        for i in range(1,len(s)):
            if s[i]==current and count<2:
                res.append(s[i])
                current=s[i]
                count+=1
                
            elif s[i]!=current:
                res.append(s[i])
                current=s[i]
                count=1
        #     print(res)
        # print(res)
        return "".join(res)


        