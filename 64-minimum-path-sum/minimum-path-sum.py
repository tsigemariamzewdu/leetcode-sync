class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        memo={}
        def dp(i,j):
            if i>=len(grid) or j>=len(grid[0]):
                return float("inf")
            if i==len(grid)-1 and j==len(grid[0])-1:
                return grid[i][j]

            state=(i,j)

            if state not in memo:
                memo[state]=grid[i][j]+min(dp(i+1,j),dp(i,j+1))
            return memo[state]
        return dp(0,0)
        