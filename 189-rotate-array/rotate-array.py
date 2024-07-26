class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)
        nums.reverse()
        l,r = 0 , k-1
        while l<r:
            nums[l],nums[r]=nums[r],nums[l]
            l +=1
            r-=1
        l,r = k , len(nums)-1
        while l<r:
            nums[l],nums[r]=nums[r],nums[l]
            l +=1
            r-=1
