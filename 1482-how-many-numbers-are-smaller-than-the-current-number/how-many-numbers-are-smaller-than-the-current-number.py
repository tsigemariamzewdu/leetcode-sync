class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sortednum=sorted(nums)
        smallercount={}

        for i,num in enumerate(sortednum):
            if num not in smallercount:
                smallercount[num]=i
        result=[]
        for num in nums:
            result.append(smallercount[num])
        return result





            
       

