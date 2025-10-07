class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def lcm(a,b):
            return (a*b)//(math.gcd(a,b))

        def checker(mid):
            pie=mid//a +mid//b+mid//c -(mid//lcm(a,b)+mid//lcm(a,c)+mid//lcm(b,c))+ mid//lcm(a,lcm(b,c))
            return pie

        left ,right=1,2*(10**9)
        while left<=right:
            mid=(left+right)//2
            if checker(mid)<n:
                left=mid+1
            elif checker(mid)>n:
                right=mid-1
            else:
                if mid %a==0 or mid%b==0 or mid %c==0:
                    return mid
                
                right=mid-1

        