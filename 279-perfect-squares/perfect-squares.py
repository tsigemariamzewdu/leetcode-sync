class Solution:
    def numSquares(self, n: int) -> int:
        memo={}

        def dp(t):
            if t==0:
                return 0
            if t<0:
                return float("inf")
            
           
            if t not in memo:

                mini=float("inf")

                for i in range(1,math.isqrt(n)+1):
                    mini=min(mini,1+dp(t-(i*i)))
                memo[t]=mini


            return memo[t]
        return dp(n)