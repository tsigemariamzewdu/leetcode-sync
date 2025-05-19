class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:

        if len(nums1)%2==0 and len(nums2) %2==0:
            return 0
        elif len(nums1) %2 !=0 and len(nums2) %2==0:
            res=0
            for i in nums2:
                res ^=i
            return res
        elif len(nums1)%2==0 and len(nums2) %2!=0:
            res=0
            for i in nums1:
                res ^=i
            return res
        else:
            res=0
            for i in nums1:
                res ^=i
            for j in nums2:
                res ^= j
            return res



        