class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        result=[0]*n
        nums.sort()
        median=nums[n//2]
        j=0
        for i in range(n):
            if nums[i]>=median:
                result[j]=nums[i]
                j+=2
                if j>=n:
                    break
        j=1
        for i in range(n):
            if nums[i]<median:
                result[j]=nums[i]
                j+=2
                if j>=n:
                    break
        return result
        
        