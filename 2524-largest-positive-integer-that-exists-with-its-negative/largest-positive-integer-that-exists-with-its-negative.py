class Solution(object):
    def findMaxK(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        i=len(nums)-1
        while i >=0 and nums[i]>0:
            if nums[i]*-1 in nums[:i]:
                return nums[i]
            i-=1
        return -1
        