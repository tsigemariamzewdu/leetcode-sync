class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n=len(points)
        root=[i for i in range(n)]
        rank=[0]*(n)
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
        lists=[]
        for i in range(len(points)):
            for j in range(i,len(points)):
                w=abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])
                lists.append([w,i,j])
        lists.sort()
        count=0
        total=0
        for i in range(len(lists)):
            if find(lists[i][1])!=find(lists[i][2]):
                union(lists[i][1],lists[i][2])
                total+=lists[i][0]
                count+=1
            if count==n-1:
                return total


        