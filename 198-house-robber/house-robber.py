class Solution:
    def rob(self, nums: List[int]) -> int:
        memo={}

        def dp(n):
            if n>=len(nums):
                return 0
            if n not in memo:
                rob=nums[n]+dp(n+2)
                skip=dp(n+1)
                memo[n]=max(rob,skip)
            return memo[n]
        return dp(0)
