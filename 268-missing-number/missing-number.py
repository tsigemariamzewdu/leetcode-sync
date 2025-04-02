class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        maxi=max(nums)
        for i in range(len(nums)+1):
            if i not in nums:
                return i
        