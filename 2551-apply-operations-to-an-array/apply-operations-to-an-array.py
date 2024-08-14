class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l=0
        j=l+1
        while j<len(nums):
            if nums[l]!=nums[j]:
                l+=1
                j+=1
            elif nums[l]==nums[j]:
                nums[l]=nums[l]*2
                nums[j]=0
                l+=1
                j+=1

        left=0
        for right in range(len(nums)):
            if nums[right]!=0:
                nums[left],nums[right]=nums[right],nums[left]
                left += 1
            
        return nums
        