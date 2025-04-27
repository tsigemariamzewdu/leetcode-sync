class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        
        graph = defaultdict(list)
        for i in range(n):
            graph[manager[i]].append(i)
 
        def dfs(node):
            maxi = 0
            for nei in graph[node]:
                total = dfs(nei)
                maxi= max(maxi, total)

            return maxi + informTime[node]

        return dfs(headID)

        