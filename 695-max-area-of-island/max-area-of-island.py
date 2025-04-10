class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
        directions=[(0,-1),(-1,0),(1,0),(0,1)]
        def in_bound(row,col):
            return  0<=row and row<len(grid) and 0<=col and col<len(grid[0])

        def dfs(visited,row,col):
            visited[row][col]=True
            answer=1
            for dr,dc in directions:
                new_row=row+dr
                new_col=col+dc
                if in_bound(new_row,new_col):

                    


                    if grid[new_row][new_col]==1 and not visited[new_row][new_col]:
                        answer += dfs(visited,new_row,new_col)
            return answer

        max_area=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1 and not visited[i][j]:
                    max_area=max(max_area,dfs(visited,i,j))

        # print(dfs(visited,min(len(grid)-1, 3), min(len(grid[0]) - 1, 8)))
        return max_area
                



