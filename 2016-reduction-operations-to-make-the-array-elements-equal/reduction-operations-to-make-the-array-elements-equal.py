class Solution(object):
    def reductionOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(reverse=True)
        current=None # this where we put the largest number 
        count=0 
        for i,num in enumerate(nums):
            if current != num:
                current=num # this means when we encounter a different number
                count +=i # we have to change all of them before it to the number that we found right so here we can do the swaps but since we are not asked to do that we can simply count how many operations does it take ?it takes i operations 
        return count # we are returning it 


        