class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        directions=[(0,1),(1,0),(0,-1),(-1,0)]
        def inbound(i,j):
            return 0<=i<rows and 0<=j<cols
        q=deque()
        o=set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    q.append((r,c,0))
                if grid[r][c]==1:
                    o.add((r,c))
        
        result=0
        while q:
            r,c,m=q.popleft()
            result=max(result,m)

            for dr,dc in directions:
                nr=r+dr
                nc=c+dc

                if inbound(nr,nc) and grid[nr][nc]==1:
                    q.append((nr,nc,m+1))
                    grid[nr][nc]=2
                    o.remove((nr,nc))
        if not o:
            return result
        return -1



        