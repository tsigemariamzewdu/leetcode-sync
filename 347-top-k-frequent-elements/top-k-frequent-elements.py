from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        res=[]
        result=[]
        counter=Counter(nums)
        for i in counter:
            result.append([i,counter[i]])
        result.sort(key=lambda list:list[1],reverse=True)
        for i in range(k):
            res.append(result[i][0])
        return res
    
       
        