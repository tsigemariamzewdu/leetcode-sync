class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        prefix=[nums[0]]*(len(nums))
        for i in range(1,len(nums)):
            prefix[i]=prefix[i-1]+nums[i]
        total=sum(nums)
        res=0

        for i in range(1,len(nums)):
            if (total-prefix[i]-prefix[i]) %2==0:
                res +=1
        return res
