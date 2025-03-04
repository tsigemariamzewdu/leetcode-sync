class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        n=len(s)
        result=[0]*n
        count1=0
        one=0
        for i in range(len(s)):
            if s[i]=="1":
                count1+=1
                if  count1>1 and one<n:
                    result[one]="1"
                    one+=1
                elif count1==1:
                    result[n-1]="1"
                    continue
        return "".join(map(str,result))
        
            
        