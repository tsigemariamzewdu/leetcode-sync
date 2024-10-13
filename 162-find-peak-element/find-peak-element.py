class Solution(object):
    def findPeakElement(self, nums):
        n = len(nums)
        if n == 1:
            return 0
        if nums[n-1] > nums[n-2]:
            return n-1
        if nums[0] > nums[1]:
            return 0

        low, high = 0, n-1
        while low <= high:
            mid = (low+high) >> 1
            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid
            elif nums[mid] < nums[mid+1]:
                low = mid + 1
            else:
                high = mid -1
        return -1

        