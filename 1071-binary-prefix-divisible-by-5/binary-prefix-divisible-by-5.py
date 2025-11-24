class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        res=[]
        num=0
        for i in nums:
            if (num*2 + i)%5==0:
                res.append(True)
            else:
                res.append(False)
            num=(num*2)+i
        return res
        