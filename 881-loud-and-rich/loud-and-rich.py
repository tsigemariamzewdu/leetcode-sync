class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:

    
        result=[i for i in range(len(quiet))]
        

        graph=defaultdict(list)
        incoming=[0 for _ in range(len(quiet))]
       
        for i in range(len(richer)):
            u,v=richer[i]
            graph[u].append(v)
            incoming[v]+=1
        q=deque()
        for i in range(len(quiet)):
            if incoming[i]==0:
                q.append(i)
       
        while q:
            print(result)
            node=q.popleft()
            for nei in graph[node]:
                if quiet[result[node]]<quiet[result[nei]]:
                   result[nei]=result[node]

                incoming[nei]-=1

                if incoming[nei]==0:
                    q.append(nei)
        return result



