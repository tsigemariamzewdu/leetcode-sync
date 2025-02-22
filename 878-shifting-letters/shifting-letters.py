class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        res=[]
        for j in s:
            res.append(ord(j)-97)
        print(res)

        prefix=[0]*(len(shifts))
        revshift=list(reversed(shifts))

        prefix[0]=revshift[0]
        for i in range(1,len(shifts)):
            prefix[i]=prefix[i-1]+revshift[i]
        normalprev=list(reversed(prefix))
        print(normalprev)
        ans=[]
        for k in range(len(res)):
           ans.append(chr((((res[k]+normalprev[k])%26)+97)))
        return "".join(ans)
