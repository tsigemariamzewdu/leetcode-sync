class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        @cache
        def dp(i,j):
            if j<0 or j==len(matrix[0]):
                return float("inf")
            if i==len(matrix):
                return 0
            return matrix[i][j]+min(dp(i+1,j-1),dp(i+1,j),dp(i+1,j+1))

        minCost=float("inf")
        for i in range(len(matrix[0])):
            minCost=min(minCost,dp(0,i))
        return minCost