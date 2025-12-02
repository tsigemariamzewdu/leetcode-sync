class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        dictt=defaultdict(int)
        mod = 10**9 + 7
        for x,y in points:
            dictt[y]+=1
        for val in dictt:
            k=dictt[val]
            dictt[val]=math.comb(k,2)
        leng=0
        for i in dictt:
            if dictt[i]!=0:
                leng+=1
        if leng<2:
            return 0
        ans=0
        total=0
        lists=[]
        for i in dictt:
            lists.append(i)
        lists.sort()
        for i in lists:
            ans += (total * dictt[i])%mod
            total+= (dictt[i])%mod
    
        return ans % ((10**9) +7)

