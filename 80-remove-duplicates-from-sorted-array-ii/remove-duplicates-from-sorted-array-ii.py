class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # two pointers
        l,r=0,0
        while r< len(nums):
            count =1
            while r+1 < len(nums) and nums[r]==nums[r+1]:
                r+=1
                count += 1
            for i in range (min(2,count)):
                nums[l]=nums[r]
                l+=1
            r+=1
        return l
        

            
        