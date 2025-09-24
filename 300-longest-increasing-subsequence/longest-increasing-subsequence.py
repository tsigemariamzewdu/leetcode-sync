class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo=[0 for _ in range(len(nums))]
        def dp(index):
            if index==len(nums):
                return 1
            if memo[index]==0:
                memo[index]=1
                for right in range(index+1,len(nums)):
                    if nums[right]>nums[index]:
                        memo[index]=max(dp(right)+1,memo[index])
            return memo[index]
        maxi=0
        for i in range(len(nums)):
            maxi=max(maxi,dp(i))
        return maxi
