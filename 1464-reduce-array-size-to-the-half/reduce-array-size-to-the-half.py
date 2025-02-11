from collections import Counter
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counter=Counter(arr)
        n=len(arr)
        h=n//2
        res=[]
        for i in counter:
            res.append(counter[i])
        res.sort(reverse=True)
        count=1
        summ=0
        for i in range(len(res)):
            if summ+res[i]>=n//2:

                return count
            else:
                summ+=res[i]
                count+=1
            

                

        
        