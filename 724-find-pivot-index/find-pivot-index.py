class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        presum=[0]*len(nums)
        sufsum=[0]*len(nums)

        presum[0]=nums[0]
        sufsum[len(nums)-1]=nums[len(nums)-1]



        for i in range(1,len(nums)):
            presum[i]=presum[i-1]+nums[i]
        for j in range(len(nums)-2,-1,-1):
            sufsum[j]=sufsum[j+1]+nums[j]
        
        for k in range(len(nums)):
            if presum[k]==sufsum[k]:
                return k
        return -1
        