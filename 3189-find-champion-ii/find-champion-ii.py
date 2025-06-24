class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        graph=defaultdict(list)
        indegree=[0 for _ in range(n)]

        ans=[]

        for u,v in edges:
            graph[u].append(v)
            indegree[v]+=1
        
        for node in range(n):
            if indegree[node]==0:
                ans.append(node)
        if len(ans)==1:
            return ans[0]
        else:
            return -1