class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo={}

        def dp(t):
            if t==target:
                return 1
            if t>target:
                return 0
            if t not in memo:
                total=0
                for num in nums:
                    total+= dp(t+num)
                memo[t]=total
            return memo[t]
        return dp(0)