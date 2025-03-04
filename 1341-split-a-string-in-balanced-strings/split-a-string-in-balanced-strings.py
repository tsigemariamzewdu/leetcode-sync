class Solution:
    def balancedStringSplit(self, s: str) -> int:
        
        countr=0

        realcount=0
        j=0
        for i in range(len(s)):
            if s[i]=="R":
                countr+=1
            else:
                countr-=1
            if countr==0:
                realcount+=1
               
        return realcount
            

        