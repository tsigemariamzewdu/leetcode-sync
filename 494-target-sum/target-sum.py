class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo={}

        def dp(i,total):
            if i >=len(nums) and target!=total:
                return 0
            elif i>=len(nums) and total==target:
                return 1
            state=(i,total)
            if state not in memo:
                memo[state]=dp(i+1,total+nums[i])+dp(i+1,total-nums[i])
            return memo[state]
        return dp(0,0)