class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter=Counter(nums)
        for i in counter:
            if counter[i]==1:
                return i
        