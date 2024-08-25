class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        stack = []
        result = [-1] * len(nums)

        for i in range(len(nums) * 2):
            val = nums[i % len(nums)]

            while stack and nums[stack[-1]] < val:
                prev = stack.pop()
                result[prev] = val
            stack.append(i % len(nums))

        return result
      
        