class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n==1:
            return [0]
        graph=defaultdict(list)

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        q=deque()
        for i in range(n):
            if len(graph[i])==1:
                q.append(i)
        remain=n
        while remain>2:
            remain-=len(q)
            for _ in range(len(q)):
                leaf=q.popleft()
                nei=graph[leaf].pop()
                graph[nei].remove(leaf)
                if len(graph[nei])==1:
                    q.append(nei)
        return list(q)

       
        # def dfs(node,visited):
        #     visited.add(node)
        #     count=0

            

        #     for nei in graph[node]:
        #         if nei not in visited:
        #             he=dfs(nei,visited)
        #             count=max(he,count)
        #     return count+1
        # answer=[]
        # mincount=float("inf")
        # mapp={}
        # for i in range(n):
        #     height=dfs(i,set())
        #     mapp[i]=height
        #     mincount=min(height,mincount)
            
        # for i in mapp:
        #     if mapp[i]==mincount:
        #         answer.append(i)
        
        return answer

            
