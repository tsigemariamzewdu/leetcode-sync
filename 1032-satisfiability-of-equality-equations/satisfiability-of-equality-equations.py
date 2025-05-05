class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        # varset=set()
        # for st in equations:
        #     varset.add(st[0])
        #     varset.add(st[3])
        # print(varset)

        root=[i for i in range(26)]
        rank=[0]*26


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
        for st in equations:
            if st[1]=="=":
                union(ord(st[0])-97,ord(st[3])-97)

        for st in equations:
            if st[1]=="!":
                
                if find(ord(st[0])-97)==find(ord(st[3])-97):
                    return False
            
          
        return True

             
            