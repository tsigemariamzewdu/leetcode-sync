class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph=[[] for _ in range(n+1)]

        for u,v,w in times:
            graph[u].append((v,w))

        
        distances = [float("inf")] *(n+1)
        distances[k] = 0
            

        queue = [k]
        while queue:
            node=heapq.heappop(queue)
            for child ,weight in graph[node]:
                new_distance=distances[node]+weight
                if new_distance< distances[child]:
                    distances[child]=new_distance
                    heapq.heappush(queue,child)
            
            
        answer= max(distances[1:])
        if answer!=float("inf"):
            return answer
        else:
            return -1
 
