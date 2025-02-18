from collections import defaultdict
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix=0
        mydict=defaultdict(int)
        mydict[0]=1
        count=0

        for num in nums:
            prefix+=num

            if prefix-goal in mydict:
                count+=mydict[prefix-goal]
            mydict[prefix]+=1
        return count


        