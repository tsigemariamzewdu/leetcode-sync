class Solution(object):
    def minSwaps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        ones=nums.count(1)
        if ones==0:
            return 0 # this is one of the edge cases
        circularNum=nums + nums # here we are adding the two nums together so that we can handle circular cases 
        nowZero=circularNum[:ones].count(0)
        minZero=nowZero

        for i  in range(ones, len(circularNum)):
            if circularNum[i]==0:
                nowZero +=1
            if circularNum[i-ones]==0:
                nowZero -=1
            minZero=min(minZero,nowZero)
        return minZero
