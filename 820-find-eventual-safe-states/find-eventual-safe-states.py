class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        result=[]
        graphh=defaultdict(list)
        indegree=[0 for _ in range(len(graph))]
        for u in range(len(graph)):
            for v in graph[u]:
                graphh[v].append(u)
                indegree[u]+=1
        print(graphh)
        print(indegree)

       

        q=deque()
        for i in range(len(graph)):
            if indegree[i]==0:
                q.append(i)
        while q:
            node=q.popleft()
            result.append(node)

            for nei in graphh[node]:
                indegree[nei]-=1

                if indegree[nei]==0:
                    q.append(nei)
        return sorted(result)