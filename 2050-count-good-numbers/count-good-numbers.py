class Solution:
    def countGoodNumbers(self, n: int) -> int:
        if n==1:
            return 5

        evenidx=ceil(n/2)
        oddidx=n//2
       
        
        def binexp(base,exponent):
            result=1
            while exponent >0:
                if exponent &1:
                    result= (result*base) % (10**9 +7)
                base = (base *base)%(10**9 +7)
                exponent >>=1
            return result

        return (binexp(5,evenidx)* binexp(4,oddidx)) % (10**9 +7)
