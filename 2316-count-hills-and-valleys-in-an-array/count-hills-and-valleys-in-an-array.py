class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        i=1
        j=i-1
        k=i+1
        count=0
        while i<len(nums)-1 and k<len(nums):
            if nums[j]>nums[i] and nums[k]>nums[i]:
                # print(nums[i],nums[j],nums[k])
                count+=1
                i=k
                j=i-1
                k=i+1
            elif nums[j]<nums[i] and nums[k]<nums[i]:
                # print(nums[i],nums[j],nums[k])
                count+=1
                i=k
                j=i-1
                k=i+1
            elif nums[i]==nums[k]:
                k+=1
            else:
                i+=1
        return count


