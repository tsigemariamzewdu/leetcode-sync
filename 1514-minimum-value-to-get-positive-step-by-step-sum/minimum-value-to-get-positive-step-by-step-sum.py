class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        cumulative_sum=0
        min_sum=0
        for num in nums:
            cumulative_sum += num
            min_sum=min(min_sum,cumulative_sum)
        startValue=1-min_sum
        return startValue
        