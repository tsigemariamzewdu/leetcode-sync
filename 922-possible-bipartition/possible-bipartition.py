class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph=defaultdict(list)

        for a,b in dislikes:
            graph[a].append(b)
            graph[b].append(a)
           
        def dfs(node,graph):
            temp=True
            for nei in graph[node]:
                if color[nei]==-1: 
                    color[nei]= 1 - color[node]
                    temp=temp and dfs(nei,graph)
                elif color[nei]==color[node]:
                    return False
            return temp
      
        color=[-1]* (n+1)
        result=True

        for node in range(n):
            if color[node]==-1:
                color[node]=0
                result=result and dfs(node,graph)
        return result


                


    

        