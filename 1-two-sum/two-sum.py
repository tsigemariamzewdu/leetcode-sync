class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mydict={}

        for i , n in enumerate(nums):
            diff=target-n
            if diff in mydict:
                return [mydict[diff],i]
            mydict[n]=i
        