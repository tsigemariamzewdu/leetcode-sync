class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        mapp={
            1:[(0,1),(0,-1)],
            2:[(1,0),(-1,0)],
            3:[(0,-1),(1,0)],
            4:[(0,1),(1,0)],
            5:[(0,-1),(-1,0)],
            6:[(0,1),(-1,0)]

        }

        def inbound(i,j):
            return 0<=i<len(grid) and 0<=j<len(grid[0])

        visited = set()  
        def dfs(i,j):
            if (i, j) in visited:      
                return False
            visited.add((i, j))

            if i==len(grid)-1 and j==len(grid[0])-1:
                return True

            for dr,dc in mapp[grid[i][j]]:
                nr=dr+i
                nc=dc+j

                if inbound(nr,nc):
                    for kr,kc in mapp[grid[nr][nc]]:
                        jr=kr+nr
                        jc=kc+nc

                        if jr==i and jc==j: 
                            if dfs(nr,nc):
                                return True
            
            return False


        
        return dfs(0,0)
        