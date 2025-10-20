class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prev=[float("inf")]*n
        prev[src]=0

        for _ in range(k+1):
            cur=prev[:]
            for u,v,w in flights:
                cur[v]=min(cur[v],prev[u]+w)
            prev=cur
        return cur[dst] if cur[dst]!=float("inf") else -1
            
        