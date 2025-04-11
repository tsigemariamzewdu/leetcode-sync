class Solution:
    def findCircleNum(self, grid: List[List[int]]) -> int:
        visited = [False]*len(grid)
     
        

        def dfs(node):
            visited[node]=True
            for  nei in range(len(grid)):
                if grid[node][nei]==1 and not visited[nei]:
                    dfs(nei)
            

        province=0
        for i in range(len(grid)):
            
                if not visited[i]:
                    dfs(i)
                    province+=1
                    

       
        return province
                




