class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        lists=defaultdict(list)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                lists[r-c].append(grid[r][c])
        
        for i in lists:
            if i>=0:
                lists[i].sort(reverse=True)
              
            else:
                lists[i].sort()
            
        ans=[[0]*len(grid[0])for _ in range(len(grid))]
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                ans[r][c]=lists[r-c].pop(0)
                
        return ans