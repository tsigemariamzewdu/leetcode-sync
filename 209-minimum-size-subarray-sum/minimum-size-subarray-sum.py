class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        res=float("inf")
        l,total=0,0
        for r in range (len(nums)):
            total += nums[r]
            while  total >= target:
                res=min(r-l+1,res)
                total -= nums[l]
                l+= 1
        return 0 if res==float("inf") else res        