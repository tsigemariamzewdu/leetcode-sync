class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp=[[0] * (r+1) for r in range(len(triangle))]

        def inbound(r,c):
            return 0<=r<len(triangle) and 0<=c<=r
        
        dp[0][0]=triangle[0][0]

        for i in range(len(triangle)):
            for j in range(i+1):
                up=float("inf")
                left=float("inf")
                if i==0 and j==0:
                    continue
                if inbound(i-1,j):
                    up=triangle[i][j]+dp[i-1][j]
                if inbound(i-1,j-1):
                    left=triangle[i][j]+dp[i-1][j-1]
                dp[i][j]=min(up,left)
        return min(dp[-1])
        