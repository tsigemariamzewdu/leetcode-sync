class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ans=nums[0]+nums[1]+nums[2]
        # since we are going to be using a two pointer we shall sort the array like now
        nums.sort()
        # we need three pointers actually since we are going to add three numbers
        for a in range(len(nums)-2):
 # why -2 since this pointer is the first pointer we need to leave exactly two places 
            if a>0 and nums[a]==nums[a-1]:
                continue
            l=a+1
            r=len(nums)-1

            while l<r:
                newsum=nums[a]+nums[l]+nums[r]
                if newsum== target:
                    return newsum
                if abs(newsum-target)<abs(ans-target):
                    ans=newsum
                if newsum > target:
                    r-=1
                if newsum < target:
                    l +=1
        return ans
