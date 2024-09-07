class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        zeros=0
        length=0

        for j in range(len(nums)):
            if nums[j]==0:
                zeros +=1
            while zeros >1:
                if nums[i]==0:
                    zeros -= 1
                i += 1
            length=max(length,j-i)
        return length




        


       
        