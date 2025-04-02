class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        maxi=max(nums)
        setn=set(nums)
        for i in range(len(nums)+1):
            if i not in setn:
                return i
        