class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """ # the nums we are given is [1,2,3,4] we are iterating in the reverse order so 
        s3=float('-inf') # this thingy right here is just to make the first condition false cause there is no number which less then s3 but we are gonna be updating s3
        stack=[] # here initializing the stack
        for i in range(len(nums)-1,-1,-1):  # iterating in the reverse order
            if nums[i]<s3:
                return True # this thing is always false unless s3 is updated so it takes at least to iteration for s3 to be update which guaranteed the length of the pattern is still satisfied
            while stack and stack[-1]<nums[i]:
                s3=stack.pop()
            stack.append(nums[i])
        return False
