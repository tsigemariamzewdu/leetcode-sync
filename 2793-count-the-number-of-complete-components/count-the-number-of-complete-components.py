class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        numset=set()
        answer=0
        for i in range(n):
            numset.add(i)
        graph=defaultdict(list)
    

        for a,b in edges:
           graph[a].append(b)
           graph[b].append(a)
        

        visited=set()
        def dfs(node):
            nonlocal node_count
            visited.add(node)
            edge_count= len(graph[node])
            node_count+=1

            
            for nei in graph[node]:
                if nei not in visited:
                    edge_count += dfs(nei)
            return edge_count
        for i in range(n):
            if i not in visited:
                node_count=0
                count=dfs(i)
                if node_count*(node_count-1)==count:
                    answer+=1
        return answer



