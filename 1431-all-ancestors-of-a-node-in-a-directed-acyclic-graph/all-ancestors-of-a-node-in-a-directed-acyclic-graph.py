class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        result=[]

        graph=defaultdict(list)

        def dfs(node,graph,visited):
            visited.add(node)
              
            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei,graph,visited)


        for x,y in edges:
            graph[y].append(x)
        
        for i in range(n):
            ancestor=[]
            visited=set()
            dfs(i,graph,visited)
            for node in range(n):
                if node==i:
                    continue
                if node in visited:
                    ancestor.append(node)
            result.append(ancestor)
        return result





        