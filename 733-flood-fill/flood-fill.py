class Solution:
    def floodFill(self, grid: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
        directions=[(0,-1),(-1,0),(1,0),(0,1)]
        def in_bound(row,col):
            return  0<=row and row<len(grid) and 0<=col and col<len(grid[0])
        value=grid[sr][sc]

        def dfs(visited,row,col):
            visited[row][col]=True
            grid[row][col]=color
            answer=1
            for dr,dc in directions:
                new_row=row+dr
                new_col=col+dc
                if in_bound(new_row,new_col) :

                    


                    if grid[new_row][new_col]== value and not visited[new_row][new_col]:
                        grid[new_row][new_col]=color
                        dfs(visited,new_row,new_col)
            return grid
        return dfs(visited,sr,sc)

      
                

