class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        root=[i for i in range(len(accounts))]
        rank=[0]*(len(accounts))

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
        mapp={}   #this is gonna map each email to the account id 
        for i,ac in enumerate(accounts):
            for j in ac[1:]:
                if j in mapp:
                    union(i,mapp[j])
                else:
                    mapp[j]=i
        group=defaultdict(list)

        for e,i in mapp.items():
            rooti=find(i)
            group[rooti].append(e)
        # print(group)
        ans=[]

        for i in group:
            result=[]
            name=accounts[i][0]
            result.append(name)
            result.extend(sorted(group[i]))
            ans.append(result)
        return ans

        
        