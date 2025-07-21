class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        counter=Counter(s)
        maxi=1
        for i in counter:
            maxi=max(maxi,counter[i])
        
      
        res=[]
        myset=set()
        for i in range(len(s)-1,-1,-1):
            if counter[s[i]]==maxi and s[i] not in myset:
                res.append(s[i])
                myset.add(s[i])
        # print(res)
        result=res[::-1]
        # print(result)
        
        return "".join(result)

        