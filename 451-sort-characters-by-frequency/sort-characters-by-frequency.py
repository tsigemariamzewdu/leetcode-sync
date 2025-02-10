from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        counter=Counter(s)
        res=[]
        result=[]
        for i in counter:
            res.append([i,counter[i]])
        res.sort(key=lambda list: list[1],reverse=True)
        for row in res:
            result.append(row[0]*row[1])
        return "".join(result)

       
        
        



        
       
        