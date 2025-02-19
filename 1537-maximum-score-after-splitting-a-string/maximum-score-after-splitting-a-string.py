class Solution:
    def maxScore(self, s: str) -> int:
        prefixsum=[0]*(len(s)+1)
        lists=list(s)
        for i in range(len(lists)):
            prefixsum[i]=prefixsum[i-1]+ int(lists[i])
        zerocount=0
        count=1 if int(lists[0])==0 else 0
        res=float("-inf") if int(lists[-1]) != 1 else 1
        for j in range(1,len(lists)-1):
            if int(lists[j])==0:
                count+=1
            cand=count+ (prefixsum[len(lists)-1]-prefixsum[j-1])
            print(cand)
            res=max(res,cand)
        if res==1:
            return res+count
        return max(res,count)

            


        