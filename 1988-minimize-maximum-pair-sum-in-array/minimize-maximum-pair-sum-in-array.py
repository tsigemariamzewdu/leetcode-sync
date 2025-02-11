class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        l=0
        r=len(nums)-1
        res=[]
        while l<r:
            pairsum=nums[l]+nums[r]
            res.append(pairsum)
            l+=1
            r-=1
        return max(res)
        