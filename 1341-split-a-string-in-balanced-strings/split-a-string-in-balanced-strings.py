class Solution:
    def balancedStringSplit(self, s: str) -> int:
        countr=0
        countl=0

        realcount=0
        j=0
        for i in range(len(s)):
            if s[i]=="R":
                countr+=1
            else:
                countl+=1
            if countr==countl:
                realcount+=1
                countr=0
                countl=0
        return realcount
            

        