class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]=nums[i]*2
                nums[i+1]=0
            else:
                nums[i]=nums[i]
            
        l=0
        for r in range(len(nums)):
            if nums[r] !=0:
                nums[l]=nums[r]
                l+=1
        while l<len(nums):
            nums[l]=0
            l+=1
        return nums




