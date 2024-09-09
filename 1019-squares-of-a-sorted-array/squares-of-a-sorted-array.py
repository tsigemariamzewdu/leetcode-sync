class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i=0
        j=len(nums)-1
        k=len(nums)-1
        result=[0]*len(nums)
        while i<=j:
            left=nums[i]**2
            right=nums[j]**2
            if left>right:
                result[k]=left
                i+=1
            else:
                result[k]=right
                j-=1
            k-=1
        return result

        