class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        directions=[(-1,0),(0,-1),(0,1),(1,0)]
        n=len(grid)
        m=len(grid[0])

        def dfs(row,col):
            if row<0 or row>=n or col<0 or col>=m or grid[row][col]==0:
                return
            grid[row][col]=0
            for dr,dc in directions:
                dfs(row+dr,col+dc)

        for i in range(n):
            if grid[i][0]==1:
                dfs(i,0)
            if grid[i][m-1]==1:
                dfs(i,m-1)
        for j in range(m):
            if grid[0][j]==1:
                dfs(0,j)
            if grid[n-1][j]==1:
                dfs(n-1,j)
        count=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    count+=1
        return count        