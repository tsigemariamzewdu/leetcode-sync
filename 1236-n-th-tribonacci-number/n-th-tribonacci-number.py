class Solution:
    def tribonacci(self, n: int) -> int:
        memo={}
        memo[0]=0
      
        memo[1]=1
        memo[2]=1

        def dp(i):
            if i not in memo:
                memo[i]=dp(i-1)+dp(i-2)+dp(i-3)
            return memo[i]
        return dp(n)