class Solution:
    def countPoints(self, rings: str) -> int:
        mapp=defaultdict(set)
        for i in range(0,len(rings)-1,2):
            mapp[rings[i+1]].add(rings[i])
            
        count=0
        print(mapp)
        for i  in mapp:
            print(mapp[i])
            if len(mapp[i])==3:
                count +=1
        return count
        