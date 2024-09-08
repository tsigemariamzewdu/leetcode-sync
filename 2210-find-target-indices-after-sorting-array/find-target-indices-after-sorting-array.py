class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums.sort()
        result=[]
        for i,num in enumerate(nums):
            if num==target:
                result.append(i)
        return result

        