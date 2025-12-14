class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count=0
        res=0
        for i in nums:
            if i==0:
                if count>0:
                    count+=1
                    res+=count
                else:
                    res+=1
                    count+=1
            else:
                count=0
            # print(res)
        return res
        