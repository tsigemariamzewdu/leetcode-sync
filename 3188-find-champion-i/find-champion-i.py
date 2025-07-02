class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        ans=[]
        for i in range(len(grid)):
            if sum(grid[i])==len(grid)-1:
                return i
                
        