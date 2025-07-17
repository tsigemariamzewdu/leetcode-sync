class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph=set()
        for road in roads:
            graph.add(tuple(road))
        degree=[0]*n

        for u,v in roads:
            degree[u]+=1
            degree[v]+=1
        maxi=0
        for i in range(n):
            for j in  range(i+1,n):
                rank=degree[i]+degree[j]
                if (i,j) in graph or (j,i) in graph:
                    rank-=1
                maxi=max(maxi,rank)
        return maxi

        