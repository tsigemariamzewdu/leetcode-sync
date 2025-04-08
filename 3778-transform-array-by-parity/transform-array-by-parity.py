class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        res=[0]*len(nums)
        for i in range(len(nums)):
            if nums[i]%2==0:
                res[i]=0
            else:
                res[i]=1
        res.sort()
        return res