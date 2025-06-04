from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        c=0
        mydict=defaultdict(int)
        prefsum=0

        mydict[0]=1

        for n in nums:
            prefsum+=n
            if prefsum-k in mydict:
                c+= mydict[prefsum-k]
            mydict[prefsum]+= 1
        return c
    