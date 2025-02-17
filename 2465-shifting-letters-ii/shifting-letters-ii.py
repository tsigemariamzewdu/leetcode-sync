class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:

        res=[]
        for j in s:
            res.append(ord(j)-97)
        
        
        prefix=[0]*len(s)
        pref=[0]*len(s)
        for  i in range(len(shifts)):
            
            if shifts[i][2]==0:
                prefix[shifts[i][0]]-=1
                if len(prefix)>shifts[i][1]+1:
                    prefix[shifts[i][1]+1]+=1
            else:
                
                prefix[shifts[i][0]]+=1
                if len(prefix)>shifts[i][1]+1:
                    prefix[shifts[i][1]+1]-=1
        pref[0]=prefix[0]
          
        for k in range(1,len(prefix)):
            pref[k]=pref[k-1]+prefix[k]
        for r in range(len(res)):
            res[r]+=pref[r]
        print(res)

        # arr=[chr(97+i) for i in range(26)]
        ress=[]
        for l in res:
         
            ress.append(chr(((l%26)+97)))
        return "".join(ress)


    