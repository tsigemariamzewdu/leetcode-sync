class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        root=[i for i in range(len(edges)+1)]
        rank=[0]* (len(edges)+1)

        def find(x):
            if x==root[x]:
                return root[x]
            root[x]=find(root[x])
            return root[x]


            
        def union(x,y):
            rootx,rooty=find(x),find(y)

            if rootx!=rooty:
                rankx=rank[rootx]
                ranky=rank[rooty]

                if rankx>ranky:
                    root[rooty]=rootx
                elif rankx<ranky:
                    root[rootx]=rooty
                else:
                    root[rooty]=rootx
                    rank[rootx]+=1
                return True
            else:
                return False
            
        for x,y in edges:
            if not union(x,y):
                return [x,y]


        
    
    