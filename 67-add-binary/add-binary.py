class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i=len(a)-1
        j=len(b)-1
        remainder=0
        result=[]

        while i >= 0 or j >= 0 or remainder:
            tot=remainder

            if i >= 0:
                tot += int(a[i])
                i -= 1
            if j >= 0:
                tot += int(b[j])
                j -= 1
            
       
            result.append(str(tot % 2))
            remainder= tot// 2
        return "".join(reversed(result))

        