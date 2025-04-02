class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter=Counter(nums)
        mini=0
        maxi=len(nums)
        
      
        buck_size=len(nums)
        buckets=[[] for i in range(buck_size+1)]
        
        for i in counter:
            buckets[counter[i]].append(i)
        result=[]
        for j in range(len(buckets)-1,-1,-1):
            if buckets[j] is not []:
            
                result.extend(buckets[j])
                if len(result)==k:
                    break
        return result

     
             
