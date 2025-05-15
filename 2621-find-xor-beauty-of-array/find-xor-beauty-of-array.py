class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        result=0
        for i in nums:
            result ^= i
        return result