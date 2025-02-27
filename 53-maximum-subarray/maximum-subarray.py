class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res=nums[0]
        maxending=nums[0]
        for i in range(1,len(nums)):
            maxending=max(maxending+nums[i],nums[i])

            res=max(maxending,res)
        return res
                

        