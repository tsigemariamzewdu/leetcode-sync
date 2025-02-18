class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        count=0
        prefix=0
        summ=0
        largest=float("-inf")
        left=0

        for right in range(len(nums)):
            # prefix+= nums[right]
            count+=nums[right]
            largest=max(largest,count)

            while count <0:
                count-=nums[left]
                left+=1
            
               
        return largest
            

        