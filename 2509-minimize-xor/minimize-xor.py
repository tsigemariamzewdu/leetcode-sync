class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        def findsetbit(n):
            res=0
            while n>0:
                res += 1 & n
                n = n>>1
            return res
        setbit1=findsetbit(num1)
        setbit2=findsetbit(num2)

        if setbit1==setbit2:
            return num1
        i=0
        x=num1
        while  setbit1>setbit2:
            if x &(1<<i):
                setbit1-=1
                x= x^(1<<i)
            i+=1
        while setbit2>setbit1:
            if x &(1<<i)==0:
   
                setbit2-=1
                x=x| (1<<i)
            i+=1
        return x

                

