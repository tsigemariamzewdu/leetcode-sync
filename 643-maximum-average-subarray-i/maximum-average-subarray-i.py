class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        wsum=sum(nums[:k])
        maxsum=wsum
        for i in range(len(nums)-k):
            wsum=wsum-nums[i]+nums[i+k]
            maxsum=max(maxsum,wsum)
        return float(maxsum)/k

        