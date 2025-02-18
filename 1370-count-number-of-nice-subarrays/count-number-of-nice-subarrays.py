from collections import defaultdict
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        mydict=defaultdict(int)
        mydict[0]=1
        prefix=0
        res=0

        count=0
        for num in nums:
            if num%2!=0:
                count+=1

            prefix+=num

            if count-k in mydict:
                res+= mydict[count-k]
            
            mydict[count]+=1
        print(mydict)
        return res


            

        