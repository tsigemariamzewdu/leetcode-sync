class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        tot=sum(nums)
        return tot%k
        