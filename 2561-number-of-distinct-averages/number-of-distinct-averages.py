class Solution(object):
    def distinctAverages(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 0 2 5 7 7 7 8 8 9 9
        average=set()
        nums.sort()
        i=0
        j=len(nums)-1
        while i<=j:
            average.add((nums[i]+nums[j])/2.0)
            i+=1
            j-=1
        return len(average)
        

        