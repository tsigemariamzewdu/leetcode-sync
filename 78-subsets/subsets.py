class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        power_set=[]
        for mask in range(1<<len(nums)):
            subset=[]
            for i in range(len(nums)):
                if mask & (1<<i):
                    subset.append(nums[i])
            power_set.append(subset)
        return power_set
