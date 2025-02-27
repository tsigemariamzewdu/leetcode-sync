class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
       
        globalmax=nums[0]
        curmax=nums[0]

        globalmin=nums[0]
        curmin=nums[0]

        for i in range(1,len(nums)):
            curmax=max(curmax+nums[i],nums[i])
            curmin=min(curmin+nums[i],nums[i])


            globalmax=max(curmax,globalmax)
            globalmin=min(curmin,globalmin)

        if globalmax<0:
            return globalmax
        else:
            return max(globalmax,(sum(nums)-globalmin))
        