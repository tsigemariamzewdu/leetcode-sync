class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo={}

        def dp(r):
            if r==0:
                return 0
            if r<0:
                return float('inf')
            if r not in memo:
                ans=float('inf')
                for c in coins:
                    ans=min(ans,1+dp(r-c))
                memo[r]=ans
            return memo[r]
        result=dp(amount)
        return result if result!=float('inf') else -1
        