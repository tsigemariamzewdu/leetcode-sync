class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.size = [1] * (size)
    def find(self, X):
        if X == self.root[X]:
            return self.root[X]
        self.root[X] =  self.find(self.root[X])
        return self.root[X]
    def union(self, X, Y):
        rootX = self.find(X)
        rootY = self.find(Y)
        if rootX != rootY:
            if self.size[rootX] > self.size[rootY]:
                self.root[rootY] = rootX
                self.size[rootX] += self.size[rootY]
            else:
                self.root[rootX] = rootY
                self.size[rootY] += self.size[rootX]
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        uf=UnionFind(len(graph))
        for u in range(len(graph)):
            if not graph[u]:
                continue
            first=graph[u][0]

            for v in graph[u]:
                if uf.find(u)==uf.find(v):
                    return False
                uf.union(first,v)
        return True
