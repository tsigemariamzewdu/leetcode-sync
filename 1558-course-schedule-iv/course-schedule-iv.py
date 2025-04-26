class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph=defaultdict(list)
        res=[]

        for u,v in prerequisites:
            graph[u].append(v)

        # print(graph)

        def bfs(start,end):
            q=deque()
            q.append(start)
            visited=set()
            
            while q:
                node=q.popleft()
                visited.add(node)

                if node==end:
                    return True
                for nei in graph[node]:
                    if nei not in visited:
                        q.append(nei)
            return False
        for qu in queries:
            res.append(bfs(qu[0],qu[1]))
        return res
