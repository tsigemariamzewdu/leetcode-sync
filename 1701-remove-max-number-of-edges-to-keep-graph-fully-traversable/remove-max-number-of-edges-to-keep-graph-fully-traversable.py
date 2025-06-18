class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size+1)]
        self.rank = [0] * (size+1)
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
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        alice=UnionFind(n)
        bob=UnionFind(n)
        keep=0

        for t,s,e in edges:
            if t==3:
                if alice.union(s,e):
                    bob.union(s,e)
                    keep+=1
        for t,s,e in edges:
            if t==1:
                if alice.union(s,e):
                    keep +=1
            if t==2:
                if bob.union(s,e):
                    keep+=1
        def isconnected(u):
            root=u.find(1)
            for i in range(2,n+1):
                if u.find(i)!=root:
                    return False
            return True
        if isconnected(alice) and isconnected(bob):
            return len(edges)-keep
        else:
            return -1