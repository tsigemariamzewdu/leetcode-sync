class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        for row in grid:
            row.sort(reverse=True)
        result=[]
        
        for i in range(len(grid)):
            for j in range(limits[i]):
                heappush(result,grid[i][j]) 
        
        while len(result)>k:
            heappop(result)
        return sum(result)
      

        