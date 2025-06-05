class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        nums=bin(n)
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                return False
        return True
        