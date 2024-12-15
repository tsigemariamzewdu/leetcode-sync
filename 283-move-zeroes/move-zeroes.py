class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # so in this question what we are supposed to do is that to move all the zeros to the last we are not asked to return anything rather to do all the things in place
        # it is a typical two pointer question 
        left=0
        for right in range(len(nums)):
            if nums[right]!=0:
                nums[left],nums[right]=nums[right],nums[left]
                left +=1
                

            

           

        