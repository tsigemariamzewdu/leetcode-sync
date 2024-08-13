class Solution(object):
    def findMiddleIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        leftmost=0
        rightmost=sum(nums)
        for i in range(len(nums)):
            rightmost-=nums[i]
            if rightmost==leftmost:
                return i 
            leftmost += nums[i]
        return -1
        