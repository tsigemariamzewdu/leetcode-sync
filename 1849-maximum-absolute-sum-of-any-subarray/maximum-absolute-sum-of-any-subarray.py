class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        res=nums[0]
        maxending=nums[0]

        for i in range(1,len(nums)):
            maxending=max(maxending+nums[i],nums[i])

            res=max(maxending,res)
        
        minn=nums[0]
        minending=nums[0]

        for j in range(1,len(nums)):
            minending=min(minending+nums[j],nums[j])

            minn=min(minending,minn)
        return max(abs(minn),res)


        