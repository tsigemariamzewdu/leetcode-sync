class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        def dfs(r,c):
            if (r<0 or c<0 or r==rows or c==cols or grid[r][c]==0 or (r,c) in visited):
                return 0
            visited.add((r,c))
            res=grid[r][c]
            directions=[[r+1,c],[r-1,c],[r,c+1],[r,c-1]]
            for dr,dc in directions:
                res += dfs(dr,dc)
            return res
        rows=len(grid)
        cols=len(grid[0])
        res=0

        visited=set()
        for r in range(rows):
            for c in range(cols):
                res= max(res,dfs(r,c))
        return res        