class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        memo={}
        
        def dp(i,total):
            if i==len(nums):
                return total==0
            state=(i,total)
            if state not in memo:
                memo[state]=dp(i+1,total-nums[i]) or dp(i+1,total)
            return memo[state]
        target=sum(nums)//2
        return sum(nums)%2==0 and dp(0,target)