class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums)<1:
            return 0
        maxdiff=0
        sorted_arr=sorted(nums)
        for i in range(len(sorted_arr)-1):
            maxdiff=max(maxdiff,sorted_arr[i+1]-sorted_arr[i])
        return maxdiff

        