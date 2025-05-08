class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        root=[i for i in range(27)]
        print(root)
        def find(x):
            if x==root[x]:
                return root[x]
            root[x]=find(root[x])
            return root[x]
     
        def union(x,y):
            rootx,rooty=find(x),find(y)

            if rootx!=rooty:
                if rootx>rooty:
                    root[rootx]=rooty
                else:
                    root[rooty]=rootx
        for i in range(len(s1)):
            ns1=ord(s1[i])-97
            ns2=ord(s2[i])-97
            union(ns1,ns2)
         

           
        
        result=[]
        for j in baseStr:
            result.append(chr(find(ord(j)-97)+97))
        return "".join(result)


