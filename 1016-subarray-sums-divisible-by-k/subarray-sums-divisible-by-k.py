from collections import defaultdict
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count=0
        mydict=defaultdict(int)
        mydict[0]=1

        prefix=0

        for num in nums:
            prefix += num

            if prefix%k in mydict:
                count+= mydict[prefix%k]
            mydict[prefix%k]+=1
            
       
        return count
                              