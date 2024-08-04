class Solution(object):
    def rangeSum(self, nums, n, left, right):
        """
        :type nums: List[int]
        :type n: int
        :type left: int
        :type right: int
        :rtype: int
        """
        newlist=[]
        for i in range (n):
            currentsum=0
            for j in range(i,n):
                currentsum += nums[j]
                newlist.append(currentsum)
        newlist.sort()
        result=sum(newlist[left-1:right])%(10**9+7)
        return result
        