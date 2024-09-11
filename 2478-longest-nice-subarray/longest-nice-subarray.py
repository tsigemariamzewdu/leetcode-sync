class Solution(object):
    def longestNiceSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
   
        n = len(nums)
        max_len = 0
        left = 0
        current_mask = 0

        for right in range(n):
            if nums[right] & current_mask == 0:
                current_mask |= nums[right]
                max_len = max(max_len, right - left + 1)
            else:
                while left <= right and (nums[right] & current_mask != 0):
                    current_mask ^= nums[left]
                    left += 1
                current_mask |= nums[right]

        return max_len


            
                 
        
        

        