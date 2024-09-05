class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res=0
        cursum=0
        prefixsum={0:1}
        
        for n in nums:
            cursum+=n
            diff=cursum-k
            res+= prefixsum.get(diff,0)
            prefixsum[cursum]=1+prefixsum.get(cursum,0)
        return res
      