class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            
            if mid > 0 and nums[mid] < nums[mid - 1]:
                return nums[mid]
            if mid < len(nums) - 1 and nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            
            
            if nums[mid] >= nums[left]:  
                left = mid + 1
            else:  
                right = mid
        
        return nums[0]  
