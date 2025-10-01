class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo={}
        def dp(i,j):
            if i>=len(triangle):
                return 0
            if j>i:
                return float("inf")
            state=(i,j)

            if state not in memo:
                memo[state]=triangle[i][j]+min(dp(i+1,j),dp(i+1,j+1))
            return memo[state]
        return dp(0,0)
        