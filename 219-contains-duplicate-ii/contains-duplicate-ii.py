class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        mapp={}

        for i,n in enumerate(nums):
            if n in mapp:
                lk=abs(mapp[n]-i)
                if lk <= k and i != mapp[n]:
                    return True 
            mapp[n]=i
        return False
           

        