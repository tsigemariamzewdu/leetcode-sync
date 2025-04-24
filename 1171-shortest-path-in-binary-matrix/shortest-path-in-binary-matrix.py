class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

    
        if not grid:
            return 0
        if grid[0][0]!=0 or grid[-1][-1]!=0:
            return -1
        def inbound(i,j):
            return 0<=i<len(grid) and 0<=j<len(grid)
        
        directions=[(0,1),(1,0),(0,-1),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
        q=deque()
        q.append((0,0,1))
        grid[0][0]=1


        
        while q:
            i,j,step=q.popleft()
           
            if i==len(grid)-1 and j==len(grid)-1:
                return step

            for dr,dc in directions:
                nr=i+dr
                nc=j+dc

                if inbound(nr,nc) and grid[nr][nc]==0:
                    grid[nr][nc]=1
                    q.append((nr,nc,step+1))
        return -1

        