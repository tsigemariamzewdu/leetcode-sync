class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo=[[0 for _ in range(n)] for _ in range(m)]

        memo[m-1][n-1]=1
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                right=memo[i][j+1] if j!=n-1 else 0
                down=memo[i+1][j] if i!=m-1 else 0
                memo[i][j]+= down +right
        return memo[0][0]
        