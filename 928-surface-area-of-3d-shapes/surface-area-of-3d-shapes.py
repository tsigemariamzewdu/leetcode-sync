class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        total=0
        count=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):

                total += 4*(grid[i][j])
                if grid[i][j]!=0:
                    count+=1
        total += count*2

        for i in range(len(grid)):
            for j in range(len(grid)):
                if 0<=i+1<len(grid):
                    total -=2* min(grid[i][j],grid[i+1][j])
                if 0<=j+1<len(grid):
                    total -= 2* min(grid[i][j],grid[i][j+1])
        return total
        