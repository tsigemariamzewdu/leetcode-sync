class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)

        for i,num in enumerate(nums):
            n = n^i^num
        return n
  
     
        