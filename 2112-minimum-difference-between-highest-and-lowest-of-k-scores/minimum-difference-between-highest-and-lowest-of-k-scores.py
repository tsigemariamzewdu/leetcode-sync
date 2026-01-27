class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k == 1:
            return 0
    
        nums.sort()
        mini = float('inf')
   
        for i in range(len(nums) - k + 1):
            diff = nums[i + k - 1] - nums[i]
            mini = min(mini, diff)
    
        return mini