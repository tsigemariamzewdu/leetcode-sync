class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res=float("-inf")
        maxending=float("-inf")
        for i in range(len(nums)):
            maxending=max(maxending+nums[i],nums[i])

            res=max(maxending,res)
        return res
                

        