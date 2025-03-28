class Solution:
    def findMin(self, nums: List[int]) -> int:
        firstarr=nums[0]
        def isvalid(mid):
            if nums[mid]>=firstarr:
                return False
            return True

        low=0
        high=len(nums)-1
        while low<=high:
            mid=(high+low)//2
            if isvalid(mid):
                high=mid-1
            else:
                low=mid+1
        if low>=0 and low<len(nums):
            return nums[low]
        return nums[low-len(nums)]