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
    def numSimilarGroups(self, strs: List[str]) -> int:
        groups=UnionFind(len(strs))
        print(groups.root)

        for i in range(len(strs)):
            curstr=strs[i]
        
            for j in range(i+1,len(strs)):
               
                checkstr=strs[j]
            
                count=0

                for k in range(len(curstr)):
                    if curstr[k]!=checkstr[k]:
                        count += 1
                if count<=2:
                    groups.union(i,j)
          
        unique_roots = set()
        for i in range(len(strs)):
            unique_roots.add(groups.find(i))
        return len(set(groups.root))


        