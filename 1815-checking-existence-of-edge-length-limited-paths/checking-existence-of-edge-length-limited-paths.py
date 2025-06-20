class UnionFind:
    def __init__(self,size):
        self.root = [i for i in range(size)]
        self.rank = [0] * (size)
    def find(self, X):
        if X != self.root[X]:
            self.root[X] = self.find(self.root[X])  
        return self.root[X]
           
     
    def union(self, X, Y):
        rootX, rootY = self.find(X), self.find(Y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootX] = rootY
                self.rank[rootY] += 1
            return True
        else:
            return False
class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        edgeList.sort(key=lambda x : x[2])
        sortedqu=sorted([(qu[0],qu[1],qu[2],i) for i, qu in enumerate(queries)],key=lambda x: x[2])
        groups=UnionFind(n)

        result=[False]*len(queries)
        idx=0

        for p,q,limit,index in sortedqu:

            while idx <len(edgeList) and edgeList[idx][2]<limit:
                u,v,path=edgeList[idx]
                groups.union(u,v)
                idx+=1
            result[index]=groups.find(p)==groups.find(q)
        return result

        