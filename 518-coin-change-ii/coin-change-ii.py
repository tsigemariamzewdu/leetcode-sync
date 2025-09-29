class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo={}

        def dp(i,r):
            if r==amount:
                return 1
            if r>amount or i==len(coins):
                return 0
            state=(i,r)
            if state not in memo:
                memo[state]=dp(i,r+coins[i])+dp(i+1,r)
            return memo[state]
        
        return dp(0,0)
        