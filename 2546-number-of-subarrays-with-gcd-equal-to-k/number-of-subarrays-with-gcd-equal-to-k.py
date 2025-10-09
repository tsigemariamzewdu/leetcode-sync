from functools import reduce
class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        count=0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                res=math.gcd(*nums[i:j+1])

               
                if res==k:

                    count+=1
        return count