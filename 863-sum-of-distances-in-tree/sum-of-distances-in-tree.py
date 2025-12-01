class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:

       
        graph=defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        count=[1]*n
        ans=[0]*n
        res=0
        def dfs(node,parent):
            
        
            for child in graph[node]:
               
                if child ==parent:
                    continue
                dfs(child,node)
                count[node]+= count[child]
                ans[0]+= count[child]
        dfs(0,-1)

        def second(node,parent):
            for child in graph[node]:
                if child==parent:
                    continue
                ans[child]=ans[node]-count[child]+ (n-count[child])
                second(child,node)
        second(0,-1)
        return  ans

            
        

       
        

                    


        